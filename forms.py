from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired
from wtforms.fields.simple import TextAreaField
from wtforms.fields.core import IntegerField, FieldList, FloatField, FormField

class ModuleForm(FlaskForm):
    name        = StringField('name', [validators.Length(min=1, max=40)])
    content     = TextAreaField('content', [validators.Length(min=1, max=5000)])
    score       = FloatField('score')
    module_id   = IntegerField('module_id')
    
    def populate(self, module):
        if isinstance(module, dict):
            self.name       = module["name"]
            self.content    = module["content"]
            self.score      = module["score"]
            self.module_id  = module["module_id"]
        else:
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
        self.id.data         = paste.id
        self.name.data       = paste.name
        self.content.data    = paste.content
        self.author.data     = paste.author
        
        self.populateModules(paste.modules)
    
    def populateModules(self, modules):  
        for module in modules:
            module_form = ModuleForm()
            module_form.populate(module)
            self.modules.append_entry(module_form)
    

    
    