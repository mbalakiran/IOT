import paho.mqtt.client as paho #mqtt library
import os
import json
import time
import logging
from datetime import datetime
from random import randint
#host name is localhost because both broker and python are Running on same
#machine/Computer.
#broker = "127.0.0.1"
broker = "mqtt.eclipseprojects.io" #host name , Replace with your IP address.
topic = "testtopic/bala"
#topicrec = "testtopic/bala1"
port = 1883 #MQTT data listening port
#ACCESS_TOKEN='M7OFDCmemyKoi461BJ4j' #not manditory

#def on_log(client, userdata, level, buf):
 #   logging.log(buf)
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
    #pass
def on_message(client, userdata, message):
    print("ACK Data is : \n")
    print(str(message.payload.decode("utf-8")))  # printing Received message
    #print("Message topic=", message.topic)
    #print("Message qos=", message.qos)
    #print("Message Retain flag= ", message.retain)

#paho.Client.connected_flag=False
client1 = paho.Client("bala_temp") #create client object
#client1.on_log = on_log
client1.on_connect = on_connect
client1.on_disconnect = on_disconnect
client1.on_publish = on_publish #assign function to callback
client1.on_message = on_message
#client1.username_pw_set(ACCESS_TOKEN) #access token from thingsboard device
client1.connect(broker, port, keepalive=60) #establishing connection
client1.loop_start()
#while not client1.connected_flag:
   # print("In wait loop")
   # time.sleep(2)
time.sleep(1)
print("Publishing data")
#publishing after every 5 secs
while True:
    #payload = "{'Temperature':10,'Humidity':50}"
    inf = {"app_id":"hajo66","dev_id":"node1","port/channel":randint(0, 100),
       "rssi":randint(0, 100),"snr":randint(0, 100),
       "sf":"SF7BW125","C_F":"C","temperature":randint(0, 100),
       "time": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
       "messgae id/counter":randint(0, 100)}
    payload = json.dumps(inf)
  #payload="{"
  #payload+="\"Temperature\":10"
  #payload+=","
  #payload+="\"Humidity\":50"
  #payload+="}"
    ret=client1.publish(topic, payload,2,True)
#ret = client1.publish(topic, payload,2,True) #topic name is test
    print(payload)
    print("Published return=",ret)
    print("Please check data on your Subscriber Code \n")
    print("ACk \n")
    client1.subscribe("testtopic/#", qos=2)
    time.sleep(10)
#client1.loop_stop()
    #client1.loop_forever()

'''

#def on_connect(client, userdata, flags, rc):
   # client.publish(topic, payload)

def on_publish(client,userdata,result): #create function for callback
  print("published data is : ", result)
  pass


client1= paho.Client("bala_temp") #create client object
#client1.on_connect = on_connect
client1.on_publish = on_publish #assign function to callback
client1.connect(broker, port, keepalive=60) #establishing connection

#publishing after every 5 secs
while True:
    payload = "{'Temperature':10,'Humidity':50}"
    ret = client1.publish(topic, payload)#, qos=2, retain=False) #topic name is test
    print(payload)
    print("Please check data on your Subscriber Code \n")
    time.sleep(1)'''