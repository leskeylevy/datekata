from . import db, login_manager
from flask_login import UserMixin
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash


# callback function for flask-login extentsion
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    avatar_hash = db.Column(db.String(32))
    follows=db.relationship('Follow',backref='users',lazy='dynamic')

    @staticmethod
    def insert_admin(email, username, password):
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

    def gravatar(self, size=40, default='identicon', rating='g'):
        url = 'https://gravatar.loli.net/avatar'
        hash = self.avatar_hash or hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(url=url, hash=hash, size=size,
                                                                     default=default, rating=rating)
    def __repr__(self):
        return f'User {self.username}'

class Follow(db.Model):
    __tablename__ = 'follows'
    followers = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    def __repr__(self):
        return f'Followed {self.follower_id}'