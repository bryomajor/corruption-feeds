import os
class Config:
    UPLOADED_PHOTOS_DEST='app/static/photos'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}