const int analogPin = 34;  // Analog input pin (adjust to your pin assignment)

void setup() {
  Serial.begin(115200);
  pinMode(34, INPUT);
}

void loop() {
  int sensorValue = analogRead(analogPin);
  double voltage = (sensorValue / 4095.0) * 5;  // Convert the ADC reading to voltage (adjust for your reference voltage)
  Serial.println(voltage, 2);  // Display voltage with 2 decimal places
  delay(1000);  // Delay for readability
}