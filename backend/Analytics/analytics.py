from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

############### Get rating ###############
getRating_URL = "http://127.0.0.1:5000/getRating"

@app.route("/getRating", methods=['GET'])
def get_rating():

  try:
    rating = request.json
    result = processGetRating(rating)
    print('\n------------------------')
    print('\nresult: ', result)
    return jsonify(result), result["code"]

  except Exception as e:
    # Unexpected error in code
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
    print(ex_str)

    return jsonify({
      "code": 500,
      "message": "analytics.py internal error: " + ex_str
    }), 500

def processGetRating(rating):
  # 2. Send the order info {cart items}
  # Invoke the order microservice
  print('\n-----Invoking rating microservice-----')
  rating_result = invoke_http(getRating_URL, method='GET',json=rating)
  print('rating_result:', rating_result)
  return {
    "code": 201,
    "data": {
      "rating_result": rating_result
    }
  }

############### Post rating ###############
postRating_URL = "http://127.0.0.1:5000/addRating"

@app.route("/addRating", methods=['POST'])
def add_rating():

  # Simple check of input format and data of the request are JSON
  if request.is_json:
    try:
      rating = request.get_json()
      print("\nReceived ratings in JSON:", rating)

      result = processPostRating(rating)
      print('\n------------------------')
      print('\nresult: ', result)
      return jsonify(result), result["code"]

    except Exception as e:
      # Unexpected error in code
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
      print(ex_str)

      return jsonify({
        "code": 500,
        "message": "analytics.py internal error: " + ex_str
      }), 500

def processPostRating(rating):
  # 2. Send the order info {cart items}
  # Invoke the order microservice
  print('\n-----Invoking rating microservice-----')
  rating_result = invoke_http(postRating_URL, method='POST', json=rating)
  print('rating_result:', rating_result)
  return {
    "code": 201,
    "data": {
      "rating_result": rating_result
    }
  }

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
  print("This is flask " + os.path.basename(__file__) + " for getting rating...")
  app.run(host="0.0.0.0", port=5100, debug=True)