import pika
from os import environ

hostname = environ.get('rabbit_host') or 'localhost'
port = environ.get('rabbit_port') or 5672

# connect to the broker
connection = pika.BlockingConnection(
  pika.ConnectionParameters(
    host=hostname, port=port,
    heartbeat=3600, blocked_connection_timeout=3600,
))

# set up a communication channel in the connection
channel = connection.channel()

# declare exchange
exchangename= "record_session_topic"
exchangetype= "topic"
channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)

# declare error queue
queue_name = 'Error'
channel.queue_declare(queue=queue_name, durable=True)

# bind error queue
routing_key = '*.error'
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=routing_key)

##########################################################################################

# checking if shared connection and channel expired, timed out, or disconnected by broker/client
# re-establish the connection/channel if they have been closed
def check_setup():
  global connection, channel, hostname, port, exchangename, exchangetype
  # check connection
  if not is_connection_open(connection):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port, heartbeat=3600, blocked_connection_timeout=3600))
  # check channel
  if channel.is_closed:
    channel = connection.channel()
    channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)

# For a BlockingConnection in AMQP clients,
# when an exception happens when an action is performed,
# it likely indicates a broken connection.
# So, the code below actively calls a method in the 'connection' to check if an exception happens
def is_connection_open(connection):
  try:
    connection.process_data_events()
    return True
  except pika.exceptions.AMQPError as e:
    print("AMQP Error:", e)
    print("...creating a new connection.")
    return False