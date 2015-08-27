# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:19:38 2015

@author: luis
"""

#project/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c=connection.cursor()
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY
    KEY AUTOINCREMENT,name TEXT NOT NULL, due_date TEXT NOT NULL,
    priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
    
    #dummy data
    c.execute("""INSERT INTO tasks(name,due_date,priority,status)
    VALUES('Finish this tutorial','03/25/2015',10,1)""")
    c.execute("""INSERT INTO tasks(name,due_date,priority,status)
    VALUES('Finish Real Python Course2','03/25/2015',10,1)""")
