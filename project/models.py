# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:27:15 2015

@author: luis
"""

#project models.py
from views import db

class Task(db.Model):
    __tablename__="tasks"
    task_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    due_date=db.Column(db.Date,nullable=False)
    priority=db.Column(db.Integer,nullable=False)
    status=db.Column(db.Integer)
    
    def __init__(self,name,due_date,priority,status):
        self.name=name
        self.due_date=due_date
        self.priority=priority
        self.status=status
    
    def repr(self):
        return '<name {0}>'.format(self.name)
        