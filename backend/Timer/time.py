from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract, func
from datetime import datetime
from flask_cors import CORS
from os import environ

app = Flask(__name__)
# set dbURL=mysql+mysqlconnector://root@localhost:3306/timer
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Timer(db.Model):
    __tablename__ = 'timer'

    timeId = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __init__(self, timeId, startDate, duration):
        self.timeId = timeId
        self.startDate = startDate
        self.duration = duration

    def json(self):
        return {"timeId": self.timeId, "startDate": self.startDate, "duration": self.duration}

# Retrieve all time records
# http://127.0.0.1:5000/getTimesAll
@app.route("/getTimesAll")
def getTimesAll():
    timeList = Timer.query.all()
    if len(timeList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "times": [time.json() for time in timeList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": "No times recorded."
        }
    ), 404

# Retrieve times this year
# http://127.0.0.1:5000/getTimesYear
@app.route("/getTimesYear")
def getTimesYear():
    timeList = Timer.query.filter(extract('year', Timer.startDate) == datetime.today().year).all()
    if timeList:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "times": [time.json() for time in timeList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": "No times found."
        }
    ), 404

# Retrieve times this month
# http://127.0.0.1:5000/getTimesMonth
@app.route("/getTimesMonth")
def getTimesMonth():
    timeList = Timer.query.filter(extract('year', Timer.startDate) == datetime.today().year).filter(extract('month', Timer.startDate) == datetime.today().month).all()
    if timeList:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "times": [time.json() for time in timeList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": "No times found."
        }
    ), 404

# Retrieve times this week
# http://127.0.0.1:5000/getTimesWeek
@app.route("/getTimesWeek")
def getTimesWeek():
    day = func.dayofweek(datetime.today())
    timeList = Timer.query.filter(extract('year', Timer.startDate) == datetime.today().year).filter(extract('month', Timer.startDate) == datetime.today().month).filter(func.dayofweek(datetime.today()) <= day).all()
    if timeList:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "times": [time.json() for time in timeList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": "No times found."
        }
    ), 404

# Add time record
# http://127.0.0.1:5000/addTime
@app.route("/addTime", methods=['POST'])
def addTime():
    data = request.get_json()
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
    app.run(host='0.0.0.0', port=5000, debug=True)