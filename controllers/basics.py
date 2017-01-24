# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from basics.py")

def home():
    message = "Are  you a "

    return locals()

def teacher(): 
    row  = db(db.course_person.person == auth.user_id).select(db.subject.course_id, db.subject.subject,  join=db.course_person.on(db.course_person.course_id == db.subject.course_id))
    
    
    gradetable = db((db.grades.teacher == auth.user_id)).select(db.grades.course_id,db.grades.student,   db.grades.score, orderby=db.grades.course_id)
   
    
    
    form = SQLFORM(db.grades).process()
  
    return locals()

Powered by web2py™ created by Massimo Di Pierro ©2007-2017 - Admin language  
