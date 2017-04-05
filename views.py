from flask import render_template
from __init__ import app, db
from models import Paste

@app.route("/")
def index():
    return render_template('index.html', nav= get_navbar())

@app.route("/paste/<int:paste_id>")
def show_paste(paste_id):
    paste= Paste.query.get(paste_id)
    if paste == None:
        return render_template('error.html', reason="Paste doesn't exist.", nav= get_navbar())
    else:
        return render_template('paste.html', paste= paste, nav= get_navbar())
    
@app.route('/paste/<int:paste_id>/remove/')
def remove_paste(paste_id):
    paste= Paste.query.get(paste_id)
    if paste == None:
        return "0"
    else:
        db.session.delete(paste)
        db.session.commit()
        return "1"
    
    
def get_navbar():
    nav= Paste.query.order_by(Paste.category).all()
    return nav