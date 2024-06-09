db = 'todolist'
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #type:ignore


class Task:
    def __init__(self , data):
        self.id = data['id']
        self.task = data['task']
        self.priority = data['priority']
        self.due_date = data['due_date']
        self.user_id = data['user_id']
        
        
        
    @classmethod
    def create(cls , data):
        query = 'insert into tasks (task , due_date , priority , user_id) values ( %(task)s , %(due_date)s , %(priority)s , %(user_id)s)'
        return connectToMySQL(db).query_db(query , data)
    
    @classmethod
    def get_all(cls):
        query = 'select * from tasks '
        return connectToMySQL(db).query_db(query)

        
        
        