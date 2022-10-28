# Publishing data using MQTT
# Author: Gustavo Bier


import paho.mqtt.client as mqtt
import json
import random
import time

# Check broker connection.

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Broker.")
    else:
        print("Fail to connect. Return code: " + str(rc))

# Set and connect client.

broker = "test.mosquitto.org"
client_id  = "UWB_sender"
topic = "UWB"

client = mqtt.Client(client_id)
client.on_connect = on_connect
client.connect(broker)
client.loop_start()

# Publishing loop.
count = 5
quality = 0
while quality < 10:
    
    # Simulating UWB message:
    x = round(random.uniform(0, 2), 5)
    y = round(random.uniform(0, 2), 5)
    z = round(random.uniform(0, 2), 5)
    msg = json.dumps({"position": {"x":x,"y":y,"z":z,"quality":quality},
                      "superFrameNumber": count})
    count += 1
    quality += 1
    client.publish(topic, msg)
    
    print("Value: " + str(msg) + ". was added to UWB topic")
    
    time.sleep(1)