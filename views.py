from flask import render_template
from __init__ import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/paste/<int:paste_id>")
def show_paste(paste_id):
    return render_template('paste.html', id= paste_id)