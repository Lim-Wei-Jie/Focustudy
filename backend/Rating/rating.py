from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
from os import environ

app = Flask(__name__)
# set dbURL=mysql+mysqlconnector://root@localhost:3306/rating
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or "mysql+mysqlconnector://root@localhost:3306/rating"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Rating(db.Model):
    __tablename__ = 'rating'
 
    ratingId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320), nullable=False)
    currentDate = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    # Constructor
    def __init__(self, ratingId, email, currentDate, rating):
        # Set the properties when created
        self.ratingId = ratingId
        self.email = email
        self.currentDate = currentDate
        self.rating = rating

# http://127.0.0.1:5001/addRating
@app.route("/addRating", methods=['POST'])
def addRating():

    data = request.get_json()
    rating = Rating(0, **data)
    
    try:
        db.session.add(rating)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": "An error occurred posting the rating."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": "Rating posted."
        }
    ), 201
    
# http://127.0.0.1:5001/getRatings
@app.route("/getRatings", methods=["POST"])
def getRatings():
    data = request.get_json()

    # For selected user, avg ratings in same date, order by date descending
    ratingList = db.session.\
        query(Rating.currentDate.label("date"), func.avg(Rating.rating).label('avgRating')).\
            group_by(Rating.currentDate).\
                order_by(Rating.currentDate.desc()).\
                    filter(Rating.email == data["email"]).\
                        all()

    if len(ratingList):
        result = []
        for rating in ratingList:
            result.append({
                "date": rating.date,
                "avgRating": round(rating.avgRating, 2)
            })
        return jsonify(
            {
                "code": 200,
                "data": {
                    "ratings": result
                }
            }
        )

    return jsonify(
        {
            # Message
            "code": 404,
            "data": "No ratings found."
        }
        # Error code
    ), 404
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)