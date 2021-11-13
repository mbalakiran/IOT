import time
import ttn
#from influxdb import InfluxDBClient
#from influxdb_client.client.write_api import SYNCHRONOUS

import json
app_id = "balaapp2"
access_key = "ttn-account-v2.13sg70NzdTkNNYQVNvGFGalygLfjqRIFadEzx5WDtrQ"
org = "balakiran"
bucket = "balakiran"
token = "5kpCX2K0Ym7OBDWv6_qh8Z1PxnS1KJ--UoNSaIte-eNVBjArPaayZUAZNgvnPc8Fdc2KkN1TsKkmsp81uAlGPg=="
ab = []
def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  #print(msg)
  ac = []
  a = [msg.payload_fields.humidity,msg.payload_fields.temperature,msg.payload_fields.led]
  ac.append(a)
  print(ac)
  ab.append(a)
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
time.sleep(60)
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