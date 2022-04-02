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

############### Get time ###############

##### Get time all #####
@app.route("/getTimesAll", methods=['POST'])
def getTimesAll():

  getTimesAll_URL = "http://127.0.0.1:5000/getTimesAll"
  # Simple check of input format and data of the request are JSON
  if request.is_json:
    try:
      allTimes = request.get_json()
      print("\nReceived all times in JSON:", allTimes)

      result = processGetTime(allTimes, getTimesAll_URL)
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

##### Get time year #####
@app.route("/getTimesYear", methods=['POST'])
def getTimesYear():

  getTimesYear_URL = "http://127.0.0.1:5000/getTimesYear"
  # Simple check of input format and data of the request are JSON
  if request.is_json:
    try:
      yearTimes = request.get_json()
      print("\nReceived all times in JSON:", yearTimes)

      result = processGetTime(yearTimes, getTimesYear_URL)
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

##### Get time month #####
@app.route("/getTimesMonth", methods=['POST'])
def getTimesMonth():

  getTimesMonth_URL = "http://127.0.0.1:5000/getTimesMonth"
  # Simple check of input format and data of the request are JSON
  if request.is_json:
    try:
      monthTimes = request.get_json()
      print("\nReceived all times in JSON:", monthTimes)

      result = processGetTime(monthTimes, getTimesMonth_URL)
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

##### Get time day #####
@app.route("/getTimesDay", methods=['POST'])
def getTimesDay():

  getTimesDay_URL = "http://127.0.0.1:5000/getTimesDay"
  # Simple check of input format and data of the request are JSON
  if request.is_json:
    try:
      dayTimes = request.get_json()
      print("\nReceived all times in JSON:", dayTimes)

      result = processGetTime(dayTimes, getTimesDay_URL)
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


# invoke helper function for get time
def processGetTime(timeReq, URL_endpoint):
  print('\n-----Invoking time microservice-----')
  times_result = invoke_http(URL_endpoint, method='POST', json=timeReq)
  print('times_result:', times_result)
  return {
    "code": 201,
    "data": {
      "times_result": times_result
    }
  }

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