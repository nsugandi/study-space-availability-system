import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("Your_MQTT_Topic")  # Subscribe to the same topic used by the ESP32

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("Your_MQTT_Broker_IP", 1883, 60)  # Use the correct broker IP and port

client.loop_forever()

def fetch_data(topic):
    pass
