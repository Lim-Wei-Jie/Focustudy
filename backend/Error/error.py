#!/usr/bin/env python3

import json
import os

import amqp_setup

monitorBindingKey='*.error'

def receiveError():
  amqp_setup.check_setup()
  
  queue_name = "Error"   

  # set up a consumer and start to wait for coming messages
  amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
  amqp_setup.channel.start_consuming()

def callback(channel, method, properties, body):
  # required signature for the callback; no return
  print("\nReceived an error by " + __file__)
  processError(body)
  print() # print a new line feed

def processError(errorMsg):
  print("Printing the error message:")
  try:
    error = json.loads(errorMsg)
    print("--JSON:", error)
  except Exception as e:
    print("--NOT JSON:", e)
    print("--DATA:", errorMsg)
  print()