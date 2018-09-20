import os


class Config:
    GITHUB_API_BASE_URL = 'https://api.github.com/search/users?q={}'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://levy:newpassword@localhost/chat'
    SECRET_KEY = os.environ.get('GITHUB_API_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
