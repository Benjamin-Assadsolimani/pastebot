from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.validators import DataRequired
from wtforms.fields.simple import TextAreaField

class PasteForm(Form):
    author      = StringField('author', [validators.Length(min=1, max=20)])
    name        = StringField('name', [validators.Length(min=1, max=20)])
    content     = TextAreaField('content', [validators.Length(min=1, max=5000)])