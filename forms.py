from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired
from wtforms.fields.simple import TextAreaField
from wtforms.fields.core import IntegerField, FieldList, FloatField
from poppler import FormField

class ModuleForm(FlaskForm):
    name        = StringField('name', [validators.Length(min=1, max=40)])
    content     = TextAreaField('content', [validators.Length(min=1, max=5000)])
    score       = FloatField('score')
    module_id   = IntegerField('module_id')
    
    def populate(self, module):
        self.name       = module.name
        self.content    = module.content
        self.score      = module.score
        self.module_id  = module.module_id
        
    
class PasteForm(FlaskForm):
    id          = IntegerField('id')
    name        = StringField('name', [validators.Length(min=1, max=20)])
    content     = TextAreaField('content', [validators.Length(min=1, max=5000)])
    author      = StringField('author', [validators.Length(min=1, max=20)])
    modules     = FieldList(FormField(ModuleForm))
    
    def populate(self, paste):
        self.id         = paste.id
        self.name       = paste.name
        self.content    = paste.content
        self.author     = paste.author
        
        for module in paste.modules:
            module_form = ModuleForm()
            module_form.populate(module)
            self.modules.append_entry(module_form)
    

    
    