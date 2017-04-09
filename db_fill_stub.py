#!/usr/bin/env python
from __init__ import db
from models import Paste, Module

p=[
Paste(content= "content-1", name="name-1", author="author-1"),
Paste(content= "content-2", name="name-2", author="author-2"),
Paste(content= "content-3", name="name-3", author="author-3"),
Paste(content= "content-4", name="name-4", author="author-4"),
Paste("content5"),
Module(name="module-1", score=0.3, content="content-mod-1", module_id=0, paste_id=1),
Module(name="module-2", score=0.7, content="content-mod-2", module_id=1, paste_id=1),
Module(name="Base64-Decoder super duper mutli mega cool", score=0.5, content="content-mod-3", module_id=0, paste_id=1),
Module(name="module-4", score=0.4, content="content-mod-4", module_id=1, paste_id=1)
]

for paste in p:
    db.session.add(paste)
db.session.commit()