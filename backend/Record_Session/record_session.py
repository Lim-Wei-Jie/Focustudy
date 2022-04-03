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

addRating_URL = environ.get('addRating_URL') or "http://localhost:5001/addRating"
addTime_URL = environ.get('addTime_URL') or "http://localhost:5002/addTime"

@app.route("/record_session", methods=["POST"])
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

  return jsonify({
    "code": 400,
    "message": "Invalid JSON input: " + str(request.get_data())
  }), 400

def processRecordSession(session_data):

  time_data = session_data['timeData']
  rating_data = session_data['ratingData']

  # TIME
  print('\n-----Invoking time microservice-----')
  time_result = invoke_http(addTime_URL, method='POST', json=time_data)

  # Check the time_result if is failure, send to error MS
  time_code = time_result["code"]

  if time_code not in range(200, 300):
    print('\n\n-----Publishing the (time error) message with routing_key=time.error-----')

    # Send time error message to Error queue
    amqp_setup.channel.basic_publish(
      exchange=amqp_setup.exchangename,
      routing_key="time.error",
      body="An error occured adding time record.",
      properties=pika.BasicProperties(delivery_mode = 2)
    )

    print("\nTime status ({:d}) published to the RabbitMQ Exchange.")

    return {
      "code": 500,
      "message": "Time record creation failure sent for error handling."
    }

  ##########################################################################

  # RATING
  print('\n-----Invoking rating microservice-----')
  rating_result = invoke_http(addRating_URL, method='POST', json=rating_data)

  # Check the rating_result if is failure, send to error MS
  rating_code = rating_result["code"]

  if rating_code not in range(200, 300):
    print('\n\n-----Publishing the (rating error) message with routing_key=rating.error-----')

    # Send rating error message to Error queue
    amqp_setup.channel.basic_publish(
      exchange=amqp_setup.exchangename,
      routing_key="rating.error",
      body="An error occured adding rating record.",
      properties=pika.BasicProperties(delivery_mode = 2)
    )

    print("\nRating status ({:d}) published to the RabbitMQ Exchange.")

    return {
        "code": 400,
        "message": "Rating record creation failure sent for error handling."
    }

  # Return created session
  return {
      "code": 201,
      "data": {
        "time_data": time_data,
        "rating_data": rating_data
      }
  }

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
  print("This is flask " + os.path.basename(__file__) + " for getting rating...")
  app.run(host="0.0.0.0", port=5100, debug=True)