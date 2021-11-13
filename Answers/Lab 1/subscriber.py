import paho.mqtt.client as paho
import time
import sys
import datetime
import json
import time
import logging
#broker = "127.0.0.1"
broker = "mqtt.eclipseprojects.io"  # host namepyth
topic = "testtopic/bala1"  # topic name


def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        logging.info("Connected OK")
    else:
        logging.info("Bad Connection", rc)
        client.loop_stop()
#def connect_msg():
 #   print("Connected to the Broker")
def on_disconnect(client, userdata,rc):
    print("Client Disconnected OK")
def on_publish(client,userdata,result): #create function for callback
    print("published data is : ", result)

def on_message(client, userdata, message):
    print("received data is :")
    print(str(message.payload.decode("utf-8")))  # printing Received message
    print("Message topic=", message.topic)
    print("Message qos=", message.qos)
    print("Message Retain flag= ", message.retain)
    #print("Received data is: ", result)


client = paho.Client("user")  # create client object
client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

print("connecting to broker host", broker)
client.connect(broker, 1883, 60)  # connection establishment with broker
print("subscribing begins here \n")
client.loop_start()
client.subscribe("testtopic/#", qos=2)  # subscribe topic test
while True:
    inf = { "Sending ACK To Device": "ACK_MSG_RECEIVED",
        "Publishing to topic": "testtopic/bala", "Payload": "ACK_MSG_RECEIVED"}
    payload = json.dumps(inf)
    ret=client.publish(topic, payload,2,True)
    #ret = client1.publish(topic, payload,2,True) #topic name is test
    print(payload)
    time.sleep(10)
#client.loop_forever()
#try:
 #   client.loop_forever()  # contineously checking for message
#except:
  #  print("Dis")


'''


#def on_connect(client, userdata, flags, rc):
   # client.subscribe(topic)
def on_message(client, userdata, message):
    print("received data is :")
    print(str(message.payload.decode("utf-8")))  # printing Received message
    print("Message topic=", message.topic)
    print("Message qos=", message.qos)
    print("Message Retain flag= ", message.retain)
    # print("Received data is: ", result)
    #print("received data is :")
    #print(str(message.payload.decode("utf-8")))  # printing Received message
    #print("")


client = paho.Client("user")  # create client object
#client.on_connect = on_connect
client.on_message = on_message

print("connecting to broker host", broker)
client.connect(broker, 1883, 60)  # connection establishment with broker
print("subscribing begins here")
client.subscribe(topic, qos=2)  # subscribe topic test

while 1:
    client.loop_forever()  # contineously checking for message'''