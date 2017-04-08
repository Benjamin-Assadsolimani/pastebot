import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_ARCHIVE                = os.path.join(basedir, 'db.old')
DATABASE_NAME                   = 'pastebot.db'
DATABASE_PATH                   = os.path.join(basedir, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI         = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS  = False

WTF_CSRF_ENABLED                = True
SECRET_KEY                      = 'e124310d6e706a3cb797baa66d2f1706a3cb797d8769221472'