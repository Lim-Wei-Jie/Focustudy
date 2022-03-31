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

getRating_URL = "http://127.0.0.1:5000/getRating"

@app.route("/getRating", methods=['GET'])
def get_rating():

  # Simple check of input format and data of the request are JSON
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
      "message": "place_order.py internal error: " + ex_str
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


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
  print("This is flask " + os.path.basename(__file__) + " for getting rating...")
  app.run(host="0.0.0.0", port=5008, debug=True)