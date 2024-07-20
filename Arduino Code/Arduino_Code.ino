#include <DHT.h>

#define DHTPIN 2          
#define DHTTYPE DHT11     
#define SOIL_MOISTURE_PIN A0 
#define PUMP_PIN 7        

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(PUMP_PIN, OUTPUT);
  dht.begin();
  Serial.println("Ready");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int moistureValue = analogRead(SOIL_MOISTURE_PIN);
  int soil_moisture = map(moistureValue, 0, 1023, 100, 0);

  Serial.print("T:");
  Serial.print(temperature);
  Serial.print(",H:");
  Serial.print(humidity);
  Serial.print(",M:");
  Serial.println(soil_moisture);

  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(PUMP_PIN, HIGH); 
      delay(1000);
      digitalWrite(PUMP_PIN, LOW);
    } else if (command == '0') {
      digitalWrite(PUMP_PIN, LOW); 
    }
  }

  delay(1000);
}

