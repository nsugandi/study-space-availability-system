import tkinter as tk
import paho.mqtt.client as mqtt

# MQTT Config
mqtt_broker = "your_mqtt_broker_address"
mqtt_topic = "your_topic_to_subscribe"

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(mqtt_topic)
    else:
        print(f"Failed to connect to MQTT Broker with code {rc}")

def on_message(client, userdata, message):
    message_data.set(message.payload.decode("utf-8"))
    update_color()

# Update color of box
def update_color():
    color = "red" if message_data.get() == "0" else "green"
    message_label.configure(bg=color)

# Create MQTT Client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT Broker
mqtt_client.connect(mqtt_broker, 1883, 60)

# Tkinter App
app = tk.Tk()
app.title("MQTT Data Display")

# Display Colored Box
message_label = tk.Label(app, text="", font=("Arial", 14), width=10, height=5)
message_label.pack(padx=20, pady=20)

# Initialize with a color based on the initial message (e.g., red or green)
message_data = tk.StringVar()
message_data.set("0")
update_color()

# Start MQTT Client
mqtt_client.loop_start()

# Tkinter Main Loop
app.mainloop()
