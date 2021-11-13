# From https://www.eclipse.org/paho/clients/python/

import paho.mqtt.client as mqtt

# test.mosquitto.org
# broker.hivemq.com
# iot.eclipse.org
THE_BROKER = 'broker.hivemq.com'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code: {str(rc)}')
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    #client.subscribe("#")
    client.subscribe("testtopic/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f'{msg.topic} {str(msg.payload)}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


print(f'Connecting to broker: {THE_BROKER}')
client.connect(THE_BROKER, 1883, 60)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
