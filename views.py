from flask import render_template, request
from __init__ import app, db
from models import Paste

@app.route("/")
def index():
    return render_template('index.html', glob_vars= get_glob_vars())

@app.route("/paste/<int:paste_id>")
def show_paste(paste_id):
    paste= Paste.query.get(paste_id)
    if paste == None:
        return index()
    else:
        return render_template('paste.html', paste= paste, glob_vars= get_glob_vars())
    
@app.route('/paste/<int:paste_id>/remove/')
def remove_paste(paste_id):
    paste= Paste.query.get(paste_id)
    if paste == None:
        return "0"
    else:
        db.session.delete(paste)
        db.session.commit()
        return "1"
    
    
def get_glob_vars():
    glob_vars= {}
    glob_vars["nav"]= Paste.query.order_by(Paste.category).all()
    glob_vars["username"]= request.cookies.get('username')
    return glob_vars