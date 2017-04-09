from flask import render_template, request, redirect, url_for
from __init__ import app, db
from models import Paste, Module
import json
import traceback
from forms import PasteForm
import sys
import module_handler

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
        paste= None
        if form.id.data != None:
            paste= Paste.query.get(form.id.data)
            if paste != None:
                paste.author= form.author.data
                paste.content= form.content.data
                paste.name= form.name.data
                
                #remove modules
                for module in paste.modules:
                    db.session.delete(module)
        
        if paste == None:    
            paste= Paste(author= form.author.data, content= form.content.data, name= form.name.data)
            db.session.add(paste)
        db.session.commit()
        
        
        for module in form.modules:
            m= Module(name= module.mod_name.data,
                      score= module.score.data, 
                      content= module.content.data, 
                      module_id= module.module_id.data, 
                      paste_id= paste.id)
            db.session.add(m)
            
        db.session.commit()

        return redirect(url_for('show_paste', paste_id=paste.id))
 
    return "0"

@app.route('/module/match', methods=['POST'])
def match_modules():
    data= getPostData()
    if data != None:
        if "data" in data:
            m= module_handler.match(data["data"])
            m.sort(key= lambda x:x["score"], reverse= True)
            paste_form= PasteForm()
            paste_form.populateModules(m)
            
            return render_template('module.html', form= paste_form)
    
    return "Error while trying to match modules!";
    


@app.route('/module/<int:module_id>/process', methods=['POST'])
def process_module(module_id):
    data= getPostData()
    
    if data != None:
        if "data" in data:
            data= data["data"]
            m= module_handler.getModule(module_id)
            if m != None:
                try:
                    return m.process(data)
                except:
                    return "Module had an error while processing data:"+str(sys.exc_info()[0])+"\n"+traceback.format_exc()
                    
    return "Error!"


def getPostData():
    if request.method == 'POST':
        if request.data:
            try:
                data= json.loads(request.data)
                return data
            except ValueError:
                return None
                    
    return None
