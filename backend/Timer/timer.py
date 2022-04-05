from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
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

# Retrieve all time records
# http://127.0.0.1:5002/getTimesAll
@app.route("/getTimesAll", methods=["POST"])
def getTimesAll():
    data = request.get_json()

    # For selected user, sum durations in same date, order by date descending
    timeList = db.session.\
        query(Timer.startDate.label("date"), func.sum(Timer.duration).label('totalDuration')).\
            group_by(Timer.startDate).\
                order_by(Timer.startDate.desc()).\
                    filter(Timer.email == data["email"]).\
                        all()

    if len(timeList):
        result = []
        for time in timeList:
            result.append({
                "date": time.date,
                "totalDuration": round(time.totalDuration / 3600, 2)
            })
        return jsonify(
            {
                "code": 200,
                "data": {
                    "times": result
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "data": "No times recorded."
        }
    ), 404

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