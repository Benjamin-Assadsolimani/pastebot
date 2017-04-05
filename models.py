from __init__ import db

class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=True)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Paste %r>' % self.id