#!/usr/bin/env python
from __init__ import app
from db_create import create_db

if __name__ == "__main__":
    create_db()
    app.run(debug=False, host="0.0.0.0")