// Include the necessary libraries
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <SPI.h>
#include <Wire.h>
#include "MQ135.h"
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Define the analog pin to which the pH sensor is connected
const int phSensorPin = A0;
//Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
 
String apiKey = "P4L2IJAOT3QT8EBI"; // Enter your Write API key from ThingSpeak
const char *ssid = "Arun";     // replace with your wifi ssid and wpa2 key
const char *pass = "";
const char* server = "api.thingspeak.com";
 
WiFiClient client;

void setup() {
  // Start serial communication at 9600 baud rate
  Serial.begin(9600);
  WiFi.begin(ssid, pass);
 
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
    Serial.println("");
    Serial.println("WiFi connected");
    
    //display.clearDisplay();
    // display.setCursor(0,0);  
    // display.setTextSize(1);
    // display.setTextColor(WHITE);
    // display.print("WiFi connected");
    // display.display();
    delay(4000);
}

void loop() {
  // Read the analog value from the pH sensor
  int sensorValue = analogRead(phSensorPin);

  // Convert the analog value to pH value (adjust according to your sensor's characteristics)
  float pHValue = map(sensorValue, 0, 1023, 0, 14); // Assuming pH range from 0 to 14

  // Print the pH value to the serial monitor
  Serial.print("pH Value: ");
  Serial.println(pHValue);

  // Add a delay before taking the next reading
  delay(1000); // Adjust according to your sampling requirements
  if (client.connect(server, 80)) // "184.106.153.149" or api.thingspeak.com
{
  String postStr = apiKey;
  postStr += "&field1="; // Field 1 on ThingSpeak
  postStr += String(phSensorPin);
  postStr += "\r\n";
  
  client.print("POST /update HTTP/1.1\n");
  client.print("Host: api.thingspeak.com\n");
  client.print("Connection: close\n");
  client.print("X-THINGSPEAKAPIKEY: " + apiKey + "\n");
  client.print("Content-Type: application/x-www-form-urlencoded\n");
  client.print("Content-Length: ");
  client.print(postStr.length());
  client.print("\n\n");
  client.print(postStr);
  
  Serial.println("Data Send to ThingSpeak");
}

client.stop();
Serial.println("Waiting...");
delay(2000);   
}
