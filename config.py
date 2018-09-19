import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://levy:newpassword@localhost/chat'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
