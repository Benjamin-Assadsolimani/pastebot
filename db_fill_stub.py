#!/usr/bin/env python
from __init__ import db
from models import Paste

p=[
Paste(content= "content-1", category="category-1", name="name-1", author="author-1"),
Paste(content= "content-2", category="category-1", name="name-2", author="author-2"),
Paste(content= "content-3", category="category-1", name="name-3", author="author-3"),
Paste(content= "content-3aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", category="categoraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay-1", name="naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaame-3", author="auaaaaaaaaaaaaaaaaaaaaaaaaaaathor-3"),
Paste("content4")
]


for paste in p:
    db.session.add(paste)
db.session.commit()