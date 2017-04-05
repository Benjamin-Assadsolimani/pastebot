from __init__ import db

class Paste(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(5000))
    category= db.Column(db.String(40))
    name    = db.Column(db.String(20))
    author  = db.Column(db.String(20))
    

    def __init__(self, content, category= "general", name= "", author= "anonymous"):
        self.content = content
        self.category= category
        self.author  = author
        self.name    = name
        
    def __repr__(self):
        return '<Paste %r>' % self.id