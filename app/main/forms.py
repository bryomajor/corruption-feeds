from flask_wtf import FlaskForm 
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Email,Required
from flask_login import current_user
from ..models import User

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('SUBMIT')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    title = StringField('Enter title',validators = [Required()])
    subtitle= StringField('Enter subtitle',validators = [Required()])
    content = TextAreaField('make a case', validators=[Required()])
    submit = SubmitField('Create Case')