#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "TP-Link_FA42";
const char* password = "TeamNowAdmitted";
const char* mqtt_server = "192.168.0.100";
const char* mqtt_topic = "seat_1";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  
  // Setup pin modes
  pinMode(2, OUTPUT); // Built-in LED
  
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  client.setServer(mqtt_server, 1883);  // Use the correct port for your broker
}

void loop() {
  if (!client.connected()) {
    if (client.connect("ESP32Client")) {
      Serial.println("Connected to MQTT broker");
    }
  }

  digitalWrite(2, HIGH); // Turn on built-in LED

  client.loop();

  // Publish data
  String payload = "Hello, MQTT!";
  client.publish(mqtt_topic, payload.c_str());
  delay(1000);  // Publish data every second
}
