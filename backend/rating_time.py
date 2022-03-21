#App to make HTTP request to other sites, usually APIs. It makes an outgoing request and returns the response from the external site
#Jsonify serializes data to JavaScript Object Notation (JSON) format
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract, func
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


db = SQLAlchemy(app)

class Rating(db.Model):
    __tablename__ = 'rating'
 
    ratingId = db.Column(db.Integer, primary_key=True)
    productivity = db.Column(db.Integer, nullable=False)

    
    #constructor
 
    def __init__(self,ratingId , productivity):
        #set the properties when created
        self.ratingId = ratingId
        self.productivity = productivity
 
        
        
    # enables our object to be represented as a JSON string
 
    def json(self):
        return {"ratingId": self.ratingId, "productivity": self.productivity}
    
    
@app.route("/posttime", methods=['POST'])
def create_rate():
    
    
    
    data = request.get_json()
    
 
    try:
        db.session.add(data)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "isbn13": "7170"
                },
                "message": "An error occurred posting the rating"
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": "rating posted"
        }
    ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    app.run(host='0.0.0.0', port=6000, debug=True)