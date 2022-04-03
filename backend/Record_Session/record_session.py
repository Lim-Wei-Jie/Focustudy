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

addRating_URL = "http://127.0.0.1:5001/addRating"
addTime_URL = "http://127.0.0.1:5002/addTime"


@app.route("/record_session", method=["POST"])
def record_session():
  # Simple check of input format and data of the request are JSON
  if request.is_json:
    try:
      session_data = request.get_json()
      print("\nReceived a session in JSON:", session_data)

      # send session info {time, ratings} to time MS and rating MS
      result = processRecordSession(session_data)
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
        "message": "record_session.py internal error: " + ex_str
      }), 500

def processRecordSession(session_data):
  rating_data = session_data
  time_data = session_data

  print('\n-----Invoking rating microservice-----')
  rating_result = invoke_http(addRating_URL, method='POST', json=rating_data)

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
  print("This is flask " + os.path.basename(__file__) + " for getting rating...")
  app.run(host="0.0.0.0", port=5100, debug=True)