from __init__ import db

class Paste(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(20))
    content = db.Column(db.String(5000))
    author  = db.Column(db.String(20))
    modules = db.relationship('Module', backref='paste', order_by='desc(Module.score)', lazy='dynamic')

    def __init__(self, content, name= "", author= "anonymous"):
        self.name    = name
        self.content = content
        self.author  = author
        
    def __repr__(self):
        return '<Paste %r (%r) by %r>' % (self.name, self.id, self.author)
    
class Module(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(40))
    content     = db.Column(db.String(5000))
    score       = db.Column(db.Integer)
    module_id   = db.Column(db.Integer)
    paste_id    = db.Column(db.Integer, db.ForeignKey('paste.id'))
    
    def __init__(self, name, score, content, module_id, paste_id):
        self.name       = name
        self.content    = content
        self.score      = score
        self.module_id  = module_id
        self.paste_id   = paste_id
    
    def __repr__(self):
        return '<Module %r (%r) with score %r, connected to paste %r>' % (self.name, self.id, self.score, self.paste_id)