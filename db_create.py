#!/usr/bin/env python
import os
import datetime
from __init__ import db
from config import DATABASE_ARCHIVE, DATABASE_PATH, DATABASE_NAME

def archive_db():
    if os.path.exists(DATABASE_PATH):
        if not os.path.exists(DATABASE_ARCHIVE):
            os.makedirs(DATABASE_ARCHIVE)
        os.rename(DATABASE_PATH, os.path.join(DATABASE_ARCHIVE, DATABASE_NAME+"-"+str(datetime.datetime.now())))
        print("created database backup!")

def create_db(force= False):
    if (not os.path.exists(DATABASE_PATH)) or force:
        archive_db()
        print "Creating new database!"
        db.create_all()

if __name__ == "__main__":
    create_db(True)