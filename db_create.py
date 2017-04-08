#!/usr/bin/env python
import os
from __init__ import db
from config import DATABASE_NAME

def create_db():
    if not os.path.exists(DATABASE_NAME):
        print "Creating new database!"
        db.create_all()

if __name__ == "__main__":
    create_db()