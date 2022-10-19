import ibmiotf.application
import ibmiotf.device
import random
import time
import sys

org_id = "nbl97v"
device_type = "weather"
device_id = "weather_id_1"
auth_method = "token"
auth_token = "Kanish@2002"



def mycmdcallback(cmd):
    print(f"Command Recieved = {str(cmd.data['command'])}")
    print(cmd)
try:
    deviceOptions = {"org" : org_id, 
                     "type" : device_type,
                     "id" : device_id,
                     "auth-method" : auth_method,
                     "auth-token" : auth_token
                    }
    deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print(f"Caught exception connecting device {str(e)}")
    sys.exit()
deviceCli.connect()
while True:
    temp = random.randint(0,100) #Temperature in Celsius
    humidity = random.randint(0,100)
    data = {"temp" : temp, "humidity" : humidity}
    print(data)
    def myonpublishcallback():
        print(f"Published Temperature  = {temp}, Humidity = {humidity}")
    success = deviceCli.publishEvent("IoTSensor","json",data,qos=1,on_publish = myonpublishcallback)
    if not success:
        time.sleep(1)
    deviceCli.commandCallback = mycmdcallback
deviceCli.disconnect()
