#!env/bin/python
from __init__ import db

def create_db():
    db.create_all()

if __name__ == "__main__":
    create_db()