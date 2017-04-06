from flask import render_template, request, redirect, url_for
from __init__ import app, db
from models import Paste
from forms import PasteForm

@app.route("/")
@app.route('/paste')
def new_paste():
    return show_paste(-1)

@app.route("/paste/<int:paste_id>")
def show_paste(paste_id):
    paste= Paste.query.get(paste_id)
    if paste == None:
        paste= Paste("")

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

@app.route('/paste/add', methods=['POST'])
def create_paste():
    form= PasteForm(request.form)
    if request.method == 'POST' :
        if form.id.data != None:
            paste= Paste.query.get(form.id.data)
            if paste != None:
                paste.author= form.author.data
                paste.content= form.content.data
                paste.name= form.name.data
                db.session.commit()
                return redirect(url_for('show_paste', paste_id=paste.id))
            
        paste= Paste(author= form.author.data, content= form.content.data, name= form.name.data)
        db.session.add(paste)
        db.session.commit()

        return redirect(url_for('show_paste', paste_id=paste.id))
 
    return "0"
    
def get_glob_vars():
    glob_vars= {}
    glob_vars["nav"]= Paste.query.order_by(Paste.category).all()
    glob_vars["username"]= request.cookies.get('username')
    glob_vars["sort_by_author"]= request.cookies.get('sort_by_author')
    glob_vars["sort_by_category"]= request.cookies.get('sort_by_category')
    glob_vars["pasteform"]= PasteForm()
    return glob_vars