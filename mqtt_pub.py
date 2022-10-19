import paho.mqtt.client as mc
import time
import random

def publish(client,usr_data,mid):
    print("Published")

client = mc.Client()
'''
client_id is the unique client id string used when connecting to the broker. 
If client_id is zero length or None, then the behaviour is defined by which protocol version is in use. 
If using MQTT v3.1.1, then a zero length client id will be sent to the broker and the broker will generate a random for the client. 
If using MQTT v3.1 then an id will be randomly generated. 
In both cases, clean_session must be True. If this is not the case a ValueError will be raised.
'''
client.on_publish = publish 
#If implemented, called when a message that was to be sent using the publish() call has completed transmission to the broker.

client.connect('broker.mqttdashboard.com', 1883)
client.loop_start()
'''
This is part of the threaded client interface. 
Call this once to start a new thread to process network traffic. This provides an alternative to repeatedly calling loop() yourself.
'''
while True:
    temperature = random.randint(0,100) #Temperature in degree Celsius
    (rc,mid) = client.publish('Temperature',str(temperature),qos=2)
    print(temperature)
    time.sleep(10)
