#!/usr/bin/env python
from __init__ import db
from models import Paste, Module

p=[
Paste(content= "content-1", category="category-1", name="name-1", author="author-1"),
Paste(content= "content-2", category="category-1", name="name-2", author="author-2"),
Paste(content= "content-3", category="category-1", name="name-3", author="author-3"),
Paste(content= "content-4", category="category-2", name="name-4", author="author-4"),
Paste("content5"),
Module("module-2", 0.4, "content-mod-2", 1),
Module("module-1", 0.3, "content-mod-1", 1),
Module("module-4", 0.7, "content-mod-4", 1),
Module("module-3", 0.5, "content-mod-3", 1)
]


for paste in p:
    db.session.add(paste)
db.session.commit()