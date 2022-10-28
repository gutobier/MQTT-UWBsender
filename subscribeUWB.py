import paho.mqtt.client as mqtt
import json

# Check broker connection.

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Broker.")
    else:
        print("Fail to connect. Return code: " + str(rc))

# Set and connect client.

broker = "test.mosquitto.org"
client_id  = "UWB_reciever"
topic = "UWB"

client = mqtt.Client(client_id)
client.on_connect = on_connect
client.connect(broker)

# Create txt files:
with open("UWB_messages.txt", "w") as file1:
    file1.write("")
    
with open("UWB_table.txt", "w") as file2:
    file2.write("")

# Callback message function

def on_message(client, userdata, msg):
    UWB = msg.payload.decode()
    print(f"Received `{UWB}` from `{msg.topic}` topic")
    uwb_dict = json.loads(UWB) # message as dictionary.
    
    # Writing in txt files:
    with open("UWB_messages.txt", "a") as file1:
        file1.write(str(uwb_dict) + "\n")
        
    with open("UWB_table.txt", "a") as file2:
        file2.write("x "+ str(uwb_dict["position"]["x"]) + "\n"
                    "y "+ str(uwb_dict["position"]["y"]) + "\n"
                    "z "+ str(uwb_dict["position"]["z"]) + "\n"
                    "quality "+ str(uwb_dict["position"]["quality"]) + "\n"
                    "superFrameNumber "+ str(uwb_dict["superFrameNumber"]) + "\n\n\n")

# Subscribing

client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
