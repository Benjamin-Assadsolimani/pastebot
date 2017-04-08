from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.validators import DataRequired
from wtforms.fields.simple import TextAreaField
from wtforms.fields.core import IntegerField

class PasteForm(FlaskForm):
    id          = IntegerField('id')
    author      = StringField('author', [validators.Length(min=1, max=20)])
    name        = StringField('name', [validators.Length(min=1, max=20)])
    content     = TextAreaField('content', [validators.Length(min=1, max=5000)])