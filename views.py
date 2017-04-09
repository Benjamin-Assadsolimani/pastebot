from flask import render_template, request, redirect, url_for
from __init__ import app, db
from models import Paste
import json
from forms import PasteForm
from modules import getModule

@app.route("/")
@app.route('/paste')
def new_paste():
    return show_paste(-1)

@app.route("/paste/<int:paste_id>")
def show_paste(paste_id):
    paste= Paste.query.get(paste_id)
    if paste == None:
        paste= Paste("")
    
    nav         = Paste.query.all()
    username    = request.cookies.get('username')
    
    paste_form  = PasteForm()
    paste_form.populate(paste)
    
    return render_template('paste.html', form= paste_form, nav= nav, username= username)
    
@app.route('/paste/<int:paste_id>/remove/')
def remove_paste(paste_id):
    paste= Paste.query.get(paste_id)
    if paste == None:
        return "0"
    else:
        for module in paste.modules:
            db.session.delete(module)
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

@app.route('/module/match', methods=['POST'])
def match_modules():
    pass
    


@app.route('/module/<int:module_id>/process', methods=['POST'])
def process_module(module_id):
    data= getData()
    if data != None:
        m= getModule(module_id)
        if m != None:
            try:
                return m.process(data)
            except:
                return "Module had an error while processing data!"
    return "Error!"


def getData():
    if request.method == 'POST':
        if request.data:
            try:
                data= json.loads(request.data)
                if "data" in data:
                    return data["data"]
            except ValueError:
                return None
                    
    return None
