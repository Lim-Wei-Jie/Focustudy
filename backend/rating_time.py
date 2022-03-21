#App to make HTTP request to other sites, usually APIs. It makes an outgoing request and returns the response from the external site
#Jsonify serializes data to JavaScript Object Notation (JSON) format
from flask import Flask, request , jsonify
from flask_cors import CORS
#Python SQL toolkit and Object Relational Mapper (ORM)
from flask_sqlalchemy import SQLAlchemy

from os import environ

# __name__ refers to your file name
app = Flask(__name__)
CORS(app)

# dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/rating'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Rating(db.Model):
    __tablename__ = 'rating'
 
    rating_id = db.Column(db.String(13), primary_key=True)
    productivity = db.Column(db.Integer, nullable=False)

    
    #constructor
 
    def __init__(self,rating_id , productivity):
        #set the properties when created
        self.rating_id = rating_id
        self.productivity = productivity
 
        
        
    # enables our object to be represented as a JSON string
 
    def json(self):
        return {"rating_id": self.rating_id, "productivity": self.productivity}
    
    
@app.route("/posttime", methods=['POST'])
def create_book():
    
    
    
    #data = request.get_json()
    rating = Rating(0, 2)
 
    try:
        db.session.add(rating)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "isbn13": "7170"
                },
                "message": "An error occurred creating the book."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": rating.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    app.run(host='0.0.0.0', port=6000, debug=True)