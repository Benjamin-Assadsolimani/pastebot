import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pastebot.db')
SQLALCHEMY_TRACK_MODIFICATIONS= False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'e124310d6e706a3cb797baa66d2f1706a3cb797d8769221472'