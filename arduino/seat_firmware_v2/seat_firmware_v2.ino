#include <WiFi.h>
#include <PubSubClient.h>
#include <stdio.h>

const char* ssid = "TP-Link_99C4";
const char* password = "85320062";
const char* mqtt_server = "192.168.0.209";
const char* mqtt_topic = "seat_1";

int previousState = -1;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  // Serial.begin(115200);
  
  // Setup pin modes
  pinMode(2, OUTPUT); // Built-in LED
  pinMode(34, INPUT); // Button
  
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    // Serial.println("Connecting to WiFi...");
  }

  client.setServer(mqtt_server, 1883);  // Use the correct port for your broker
}

void loop() {
  if (!client.connected()) {
    if (client.connect("Seat_2")) {
      // Serial.println("Connected to MQTT broker");
    }
  }

  digitalWrite(2, HIGH); // Turn on built-in LED

  client.loop();

  // Publish data
  // 0 means unoccupied, 1 means occupied
  int currentState = (digitalRead(34) + 1) % 2; // flip ones and zeros
  if (currentState != previousState) {
    // Serial.println(currentState);
    String payload = String(currentState);
    client.publish(mqtt_topic, payload.c_str());
  }
  previousState = currentState;
  delay(1000);
}
