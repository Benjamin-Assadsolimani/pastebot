from __init__ import db

class Paste(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(5000))
    category= db.Column(db.String(40))
    name    = db.Column(db.String(20))
    author  = db.Column(db.String(20))
    modules = db.relationship('Module', backref='paste', order_by='desc(Module.score)', lazy='dynamic')

    

    def __init__(self, content, category= "general", name= "", author= "anonymous"):
        self.content = content
        self.category= category
        self.author  = author
        self.name    = name
        
    def __repr__(self):
        return '<Paste %r (%r) by %r>' % (self.name, self.id, self.author)
    
class Module(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(40))
    score   = db.Column(db.Integer)
    content = db.Column(db.String(5000))
    paste_id= db.Column(db.Integer, db.ForeignKey('paste.id'))
    
    def __init__(self, name, score, content, paste_id):
        self.name= name
        self.score= score
        self.content= content
        self.paste_id= paste_id
    
    def __repr__(self):
        return '<Module %r (%r) with score %r, connected to paste %r>' % (self.name, self.id, self.score, self.paste_id)