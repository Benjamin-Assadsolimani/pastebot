from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired
from wtforms.fields.simple import TextAreaField
from wtforms.fields.core import IntegerField, FieldList, FormField, DecimalField

class ModuleForm(FlaskForm):
    mod_name    = StringField('mod_name', [validators.Length(min=1, max=40)])
    content     = TextAreaField('content', [validators.Length(min=1, max=5000)])
    score       = DecimalField('score', places=2)
    module_id   = IntegerField('module_id')
    expanded    = IntegerField('expanded')
    
    def populate(self, module):
        if isinstance(module, dict):
            self.mod_name   = module["name"]
            self.content    = module["content"]
            self.score      = module["score"]
            self.module_id  = module["module_id"]
            self.expanded   = module["expanded"]
        else:
            self.mod_name   = module.name
            self.content    = module.content
            self.score      = module.score
            self.module_id  = module.module_id
            self.expanded   = 0 if module.content == "" else 1
    
    def __repr__(self):
        return "ModuleForm <name: "+self.name+", content: "+self.content+", score: "+str(self.score)+", module_id: "+self.module_id+">"            
        
    
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
    

    
    