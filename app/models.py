import hashlib
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin


# callback function for flask-login extentsion
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    avatar_hash = db.Column(db.String(32))

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
        # if request.is_secure:
        #     url = 'https://secure.gravatar.com/avatar'
        # else:
        #     url = 'http://www.gravatar.com/avatar'
        url = 'https://gravatar.loli.net/avatar'
        hash = self.avatar_hash or hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(url=url, hash=hash, size=size,
                                                                     default=default, rating=rating)


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)


class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('comments.id'), primary_key=True)



# class Comment ( db.Model ):
#     __tablename__ = 'comments'
#     id = db.Column ( db.Integer , primary_key=True )
#     content = db.Column ( db.Text )
#     timestamp = db.Column ( db.DateTime , default=datetime.utcnow )
#     author_name = db.Column ( db.String ( 64 ) )
#     author_email = db.Column ( db.String ( 64 ) )
#     avatar_hash = db.Column ( db.String ( 32 ) )
#     article_id = db.Column ( db.Integer , db.ForeignKey ( 'articles.id' ) )
#     disabled = db.Column ( db.Boolean , default=False )
#     comment_type = db.Column ( db.String ( 64 ) , default='comment' )
#     reply_to = db.Column ( db.String ( 128 ) , default='notReply' )
#
#     followed = db.relationship ( 'Follow' , foreign_keys=[Follow.follower_id] ,
#                                  backref=db.backref ( 'follower' , lazy='joined' ) , lazy='dynamic' ,
#                                  cascade='all, delete-orphan' )
#     followers = db.relationship ( 'Follow' , foreign_keys=[Follow.followed_id] ,
#                                   backref=db.backref ( 'followed' , lazy='joined' ) , lazy='dynamic' ,
#                                   cascade='all, delete-orphan' )
#
#     def __init__(self , **kwargs):
#         super ( Comment , self ).__init__ ( **kwargs )
#         if self.author_email is not None and self.avatar_hash is None:
#             self.avatar_hash = hashlib.md5 ( self.author_email.encode ( 'utf-8' ) ).hexdigest ( )
#
#     def gravatar(self , size=40 , default='identicon' , rating='g'):
#         # if request.is_secure:
#         #     url = 'https://secure.gravatar.com/avatar'
#         # else:
#         #     url = 'http://www.gravatar.com/avatar'
#         url = 'https://gravatar.loli.net/avatar'
#         hash = self.avatar_hash or hashlib.md5 ( self.author_email.encode ( 'utf-8' ) ).hexdigest ( )
#         return '{url}/{hash}?s={size}&d={default}&r={rating}'.format ( url=url , hash=hash , size=size ,
#             default=default , rating=rating )
