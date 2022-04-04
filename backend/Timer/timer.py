from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract, and_, func
from datetime import date, timedelta
from flask_cors import CORS
from os import environ

app = Flask(__name__)
# set dbURL=mysql+mysqlconnector://root@localhost:3306/timer
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or "mysql+mysqlconnector://root@localhost:3306/timer"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Timer(db.Model):
    __tablename__ = 'timer'

    timeId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320), nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __init__(self, timeId, email, startDate, duration):
        self.timeId = timeId
        self.email = email
        self.startDate = startDate
        self.duration = duration

# Add time record
# http://127.0.0.1:5002/addTime
@app.route("/addTime", methods=['POST'])
def addTime():
    data = request.get_json()

    # PRI KEY auto increment
    time = Timer(0, **data)

    try:
        db.session.add(time)
        db.session.commit()

    except:
        return jsonify(
            {
                "code": 500,
                "data": "An error occurred creating time record."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": "New time recorded."
        }
    ), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)