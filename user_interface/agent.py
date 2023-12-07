import tkinter as tk
import paho.mqtt.client as mqtt
import csv

# MQTT Config
mqtt_broker = "192.168.0.209"
mqtt_topic = "room_1/seat_1"

Seats = {}

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(mqtt_topic)
    else:
        print(f"Failed to connect to MQTT Broker with code {rc}")

def on_message(client, userdata, message):
    # turns message into an array of [status, ip address]
    curr_message = message.payload.decode("utf-8").split()
    status = curr_message[0]
    ip_address = curr_message[1]
    Seats.update({ip_address: status})
    print(Seats)
    update_csv()

def update_csv():
    with open('availability.csv', 'w') as f:
    # Write all the dictionary keys in a file with commas separated.
        for key in Seats.keys():
            string = key + "," + Seats.get(key) + "\n"
            f.write(string)

# Create MQTT Client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT Broker
mqtt_client.connect(mqtt_broker, 1883, 60)

# Start MQTT Client
mqtt_client.loop_forever()
