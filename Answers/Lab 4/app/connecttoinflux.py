#from t2 import ab
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import InfluxDBClient
#print(ab)
org = "balakiran"
bucket = "collect"
token = "5kpCX2K0Ym7OBDWv6_qh8Z1PxnS1KJ--UoNSaIte-eNVBjArPaayZUAZNgvnPc8Fdc2KkN1TsKkmsp81uAlGPg=="

#establish a connection
client = influxdb_client.InfluxDBClient(url="http://localhost:8086", token=token, org=org)

#instantiate the WriteAPI and QueryAPI
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
#write_api.write("my-bucket", "my-org", [{"measurement": "h2o_feet", "tags": {"location": "coyote_creek"}, "fields": {"water_level": 1}, "time": 1}])
#create and write the point
p = influxdb_client.Point("mysensordata").field("Temperature", 10.0).field("Humidity", 30.0).field("Led", 1)
write_api.write(bucket=bucket,org=org,record=p)
#return the table and print the result