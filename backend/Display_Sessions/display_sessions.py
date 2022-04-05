import email
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

displayRating_URL = environ.get('displayRating_URL') or "http://localhost:5001/getRatings"
displayTime_URL = environ.get('displayTime_URL') or "http://localhost:5002/getTimesAll"

@app.route("/display_sessions", methods=["POST"])
def display_sessions():
  # Simple check of input format and data of the request are JSON
  if request.is_json:
    try:
      email = request.get_json()
      print("\nReceived email in JSON:", email)

      # send email info {email} to time MS and rating MS
      result = processAllSessions(email)
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
        "message": "display_sessions.py internal error: " + ex_str
      }), 500

  return jsonify({
    "code": 400,
    "message": "Invalid JSON input: " + str(request.get_data())
  }), 400

def processAllSessions(email):

  # TIME
  print('\n-----Invoking time microservice-----')
  time_result = invoke_http(displayTime_URL, method='POST', json=email)
  print(time_result)
  # Check the time_result if is failure, send to error MS
  time_code = time_result["code"]

  if time_code not in range(200, 300):
    print('\n\n-----Publishing the (time error) message with routing_key=time.error-----')

    # Send time error message to Error queue
    amqp_setup.channel.basic_publish(
      exchange=amqp_setup.exchangename,
      routing_key="time.error",
      body="An error occured retrieving time record.",
      properties=pika.BasicProperties(delivery_mode = 2)
    )

    print("\nTime status ({:d}) published to the RabbitMQ Exchange.")

    return {
      "code": 500,
      "message": "Time record retrieval failure sent for error handling."
    }

  ##########################################################################

  # RATING
  print('\n-----Invoking rating microservice-----')
  rating_result = invoke_http(displayRating_URL, method='POST', json=email)
  print(rating_result)
  # Check the rating_result if is failure, send to error MS
  rating_code = rating_result["code"]

  if rating_code not in range(200, 300):
    print('\n\n-----Publishing the (rating error) message with routing_key=rating.error-----')

    # Send rating error message to Error queue
    amqp_setup.channel.basic_publish(
      exchange=amqp_setup.exchangename,
      routing_key="rating.error",
      body="An error occured retrieving rating record.",
      properties=pika.BasicProperties(delivery_mode = 2)
    )

    print("\nRating status ({:d}) published to the RabbitMQ Exchange.")

    return {
        "code": 400,
        "message": "Rating record retrieval failure sent for error handling."
    }

  # Return retrieved data
  return {
      "code": 201,
      "data": {
        "time_data": time_result,
        "rating_data": rating_result
      }
  }

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
  print("This is flask " + os.path.basename(__file__) + " for getting time and rating...")
  app.run(host="0.0.0.0", port=5200, debug=True)