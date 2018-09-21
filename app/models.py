import hashlib
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager


language_types = {u'Web development': ['Python', 'Java', 'JavaScript'],
                 'Linux': [u'Linux', u'Linux', 'CentOS', 'Ubuntu'],
                 u'Mobile development': [u'swift', u'java'],
                 u'Data Science': ['MySQL', 'Redis'],
                 u'Application Development，': [u'swift', u'ruby',u'python'],
                 u'Web': ['Flask', 'Django'],}


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
    def insert_admin(email , username , password):
        user = User ( email=email , username=username , password=password )
        db.session.add ( user )
        db.session.commit ( )

    @property
    def password(self):
        raise AttributeError ( 'password is not a readable attribute' )

    @password.setter
    def password(self , password):
        self.password_hash = generate_password_hash ( password )

    def verify_password(self , password):
        return check_password_hash ( self.password_hash , password )

    def __init__(self , **kwargs):
        super ( User , self ).__init__ ( **kwargs )
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5 ( self.email.encode ( 'utf-8' ) ).hexdigest ( )

    def gravatar(self , size=40 , default='identicon' , rating='g'):
        # if request.is_secure:
        #     url = 'https://secure.gravatar.com/avatar'
        # else:
        #     url = 'http://www.gravatar.com/avatar'
        url = 'https://gravatar.loli.net/avatar'
        hash = self.avatar_hash or hashlib.md5 ( self.email.encode ( 'utf-8' ) ).hexdigest ( )
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format ( url=url , hash=hash , size=size ,
            default=default , rating=rating )



class Follow ( db.Model ):
        __tablename__ = 'follows'
        follower_id = db.Column ( db.Integer , db.ForeignKey ( 'user.id' ) , primary_key=True )
        followed_id = db.Column ( db.Integer , db.ForeignKey ( 'user.id' ) , primary_key=True )



class Language (UserMixin,db.Model ):
    '''
    Pitch class to define Post Objects
    '''
    __tablename__ = 'languages'

    id = db.Column ( db.Integer , primary_key=True )
    languages = db.Column ( db.String )
    category_id = db.Column ( db.Integer )
    user_id = db.Column ( db.Integer , db.ForeignKey ( "user.id" ) )


class LanguageCategory ( UserMixin,db.Model ):
    '''
    Function that defines different categories of posts
    '''
    __tablename__ = 'language_categories'

    id = db.Column ( db.Integer , primary_key=True )
    name_of_category = db.Column ( db.String ( 255 ) )
    category_description = db.Column ( db.String ( 255 ) )

    @classmethod
    def get_categories(cls):
        '''
        This function fetches all the categories from the database
        '''
        categories = LanguageCategory.query.all ( )
        return categories
