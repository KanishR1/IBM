import paho.mqtt.client as mc
import time

def subscribe(client,usrdata,mid, granted_qos):
    print(f"Subscribe : {mid} Qos : {granted_qos}")

def on_message(client,usrdata,msg):
    print(f"{msg.topic} {msg.qos} {str(msg.payload)[2:-1]}")

client = mc.Client()
client.on_subscribe = subscribe
client.on_message = on_message
client.connect("broker.mqttdashboard.com",1883)
client.subscribe('Temperature', qos = 2)
client.loop_forever()

