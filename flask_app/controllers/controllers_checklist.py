from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.controllers import controllers_users
from flask_app.models.models_task import Task
from flask_app.models import models_task

@app.route('/create')
def home():
    return render_template('createtask.html')

@app.route('/showtask' , methods=['POST'])
def verify():
    data = {'task' :request.form['task'] , 
            'due_date':request.form['due_date'],
            'priority':request.form['priority'],
            'user_id':request.form['user_id']
            }
    Task.create(data)
    return redirect('/showalltasks')

@app.route('/showalltasks')
def showall():
    task = Task.get_all()
    return render_template('showall.html'  , task = task )