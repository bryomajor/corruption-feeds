from flask import Flask 
from config import config_options
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES
photos = UploadSet('photos', IMAGES)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstap = Bootstrap()
db = SQLAlchemy()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint


    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    
    bootstap.init_app(app)

    # Configure UploadSet
    configure_uploads(app,photos)
    
    db.init_app(app)
    login_manager.init_app(app)



    return app