from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
db = 'todolist'
r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.username = data['username']
        
        
    @classmethod
    def get_by_username(cls , data):
        query = 'select * from users where username = %(username)s'
        return connectToMySQL(db).query_db(query ,  data)
    
    @classmethod
    def register(cls , data):
        query = 'insert into users (first_name , last_name , username)  values (%(first_name)s   ,   %(last_name)s     ,       %(username)s )'
        return connectToMySQL(db).query_db(query , data)
    
