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


class CaseForm(FlaskForm):
    title = StringField('Enter Title',validators = [Required()])
    subtitle= StringField('Enter Location',validators = [Required()])
    content = TextAreaField('Make a Case', validators=[Required()])
    submit = SubmitField('Create Case')