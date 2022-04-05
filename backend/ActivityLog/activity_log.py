import json
import os

import amqp_setup

monitorBindingKey='#.log'

def receiveSessionLog():
    amqp_setup.check_setup()
        
    queue_name = 'Activity_Log'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming()

def callback(channel, method, properties, body):
    print("\nReceived a session log by " + __file__)
    processSessionLog(body)
    print()

def processSessionLog(data):
    print("Recording session log:")
    print(data)

if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveSessionLog()