import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_NAME= os.path.join(basedir, 'pastebot.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_NAME
SQLALCHEMY_TRACK_MODIFICATIONS= False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'e124310d6e706a3cb797baa66d2f1706a3cb797d8769221472'