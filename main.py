'''
@author: DerBenOo
'''

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/scratchpad.html")
def scratchpad():
    return render_template('scratchpad.html')

if __name__ == "__main__":
    app.run()