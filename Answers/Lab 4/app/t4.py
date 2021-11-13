import time
import ttn
#from influxdb import InfluxDBClient
#from influxdb_client.client.write_api import SYNCHRONOUS

import json
app_id = "campusborlangeelsys"
access_key = "ttn-account-v2.seLvoth60Fkd5u8Y7Faky86PHUBldhMqLPHVpqKE66Q"
#discovery.thethingsnetwork.org:1900
def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print(msg)
  #ac = []
  #a = [msg.payload_fields.humidity,msg.payload_fields.temperature,msg.payload_fields.led]
  #ac.append(a)
  #print(ac)
  #ab.append(a)
  #ab.append(json.dumps(msg))
  #print(ab)
  #print("As JSON: ", ab)

#client = InfluxDBClient(host='localhost', port=8086)
handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
#mqtt_client.forever()
time.sleep(10000)
mqtt_client.close()

# using application manager client
app_client = handler.application()
my_app = app_client.get()
#print(my_app)

my_devices = app_client.devices()
print(my_devices)
#ab = json.dumps(my_devices)
print(ab)
#print(ab)