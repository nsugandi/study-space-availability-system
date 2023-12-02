import tkinter as tk
import paho.mqtt.client as mqtt

# MQTT Config
mqtt_broker = "192.168.0.161"
mqtt_topic = "seat_1"

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


# Create MQTT Client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT Broker
mqtt_client.connect(mqtt_broker, 1883, 60)

# Start MQTT Client
mqtt_client.loop_start()
