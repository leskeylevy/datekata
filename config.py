import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://feisal:1234@localhost/kata'
    # GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # CLIENT_ID = os.environ.get('CLIENT_ID')
    # CLIENT_SECRET =os.environ.get('CLIENT_SECRET')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
