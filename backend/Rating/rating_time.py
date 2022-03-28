#App to make HTTP request to other sites, usually APIs. It makes an outgoing request and returns the response from the external site
#Jsonify serializes data to JavaScript Object Notation (JSON) format
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ


app = Flask(__name__)
# set dbURL=mysql+mysqlconnector://root@localhost:3306/rating 
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Rating(db.Model):
    __tablename__ = 'rating'
 
    ratingId = db.Column(db.Integer, primary_key=True)
    productivity = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(320), nullable=False)
    currentDate = db.Column(db.String(320), nullable=False)
    partDay = db.Column(db.String(320), nullable=False)
    morningGPA = db.Column(db.Integer, nullable=False)
    afternoonGPA = db.Column(db.Integer, nullable=False)
    nightGPA = db.Column(db.Integer, nullable=False)


    
    # constructor
    def __init__(self,ratingId , productivity,email,currentDate,partDay,morningGPA,afternoonGPA,nightGPA):
        #set the properties when created
        self.ratingId = ratingId
        self.productivity = productivity
        self.email = email
        self.partDay = partDay
        self.currentDate= currentDate
        self.morningGPA= morningGPA
        self.afternoonGPA= afternoonGPA
        self.nightGPA = nightGPA
        
    # enables our object to be represented as a JSON string
    def json(self):
        return {"ratingId": self.ratingId, "productivity": self.productivity,"email": self.email,"currentDate":self.currentDate,"partDay":self.partDay,"morningGPA":self.morningGPA,"afternoonGPA":self.afternoonGPA, "nightGPA":self.nightGPA}

# http://127.0.0.1:5000/addRating
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
                "data": "An error occurred posting the rating"
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": "Rating posted"
        }
    ), 201
    
    
@app.route("/getRating")
def getRating():
    #select * from rating
    ratinglist = Rating.query.all()
    print(type(ratinglist))
    if len(ratinglist):
        
        #return in json format
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #create a json representation for each book
                    "ratings": [ rating.json() for rating in ratinglist]
                }
            }
        )
    return jsonify(
        {
            #message
            "code": 404,
            "message": "There are no books."
        }
        #error code
    ), 404
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)