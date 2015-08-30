# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:19:38 2015

@author: luis
"""

#project/db_create.py
from views import db
from models import Task
from datetime import date

#create the database and db table

db.create_all()
db.session.add(Task("Finish this tutorial",date(2015,3,13),10,1))
db.session.add(Task("Finish Real Python",date(2015,3,13),10,1))

db.session.commit()
