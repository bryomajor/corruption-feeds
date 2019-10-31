import os
class Config:
    UPLOADED_PHOTOS_DEST='app/static/photos'
    SECRET_KEY='noneofyb'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:p@$$w0rd@localhost/feeds'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}