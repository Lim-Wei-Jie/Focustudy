from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/TaskList'
app.config['SQLALEHCMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

@app.route("/task_list/<string:email>")
def tasklist_by_email(email):

    initial = TaskList.query.filter_by(email=email)
    task_list = {}

    for task in initial:
        converted = task.__dict__
        converted.pop("_sa_instance_state")
        converted.pop("email")
        task_id = converted["task_id"]
        converted.pop("task_id")
        task_list[task_id] = converted

    if task_list:
        return jsonify (
            {
                "code": 200,
                # "data": task_list.json()
                "data": task_list
            }
        ), 200

    return jsonify (
        {
           "code": 404,
            "message": "No tasks in task list." 
        }
    ), 404

@app.route("/task_list/<string:email>", methods=['POST'])
def create_task(email):

    all_tasks = TaskList.query.filter_by(email=email)
    data = request.get_json()

    for task in all_tasks:
        if task.__dict__["task_description"] == data["task_description"]:
            return jsonify (
                {
                    "code": 400,
                    "message": "Task already exists."
                }
            ), 400

    task = TaskList(email, **data)

    try:
        db.session.add(task)
        db.session.commit()
    except:
        return jsonify (
            {
                "code": 500,
                "data": {
                    "email": email
                },
                "message": "An error occured creating the task."
            }
        ), 500

    return jsonify (
        {
            "code": 201,
            "data": task.json()
        }
    ), 201

class TaskList(db.Model):
    __tablename__ = 'task_list'
    
    task_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    task_description = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=True)
 
    def __init__(self, email, task_description, status):
        self.email = email
        self.task_description = task_description
        self.status = status
 
    def json(self):
        return {"email": self.email, "task_description": self.task_description, "status": self.status}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)