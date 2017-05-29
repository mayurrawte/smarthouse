import paho.mqtt.client as mqtt
import requests
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("smarthouse112/update/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    device = (msg.topic).replace('smarthouse112/update/','')
    print device
    print type(msg.payload)
    x =  json.loads(msg.payload)
    r = requests.post("http://127.0.0.1:8000/update/"+device+"/",data=x)
    print r.text

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

client.loop_forever()
