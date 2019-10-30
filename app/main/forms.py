from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Email,Required
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Email,Required
from flask_login import current_user
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')