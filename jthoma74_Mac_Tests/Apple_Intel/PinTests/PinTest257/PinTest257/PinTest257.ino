#include <Servo.h>

/**
 * Testing pin maps using Analog read input on Arduino
 */

int outputPin = 35;  // pin to test
int inputPin = 2;    // input pin to read from output pin
int val = 0;      // variable to store read value

void setup() {
  Serial1.begin(9600);
  pinMode(outputPin, OUTPUT);  // sets pin as output
  pinMode(inputPin, INPUT);    // sets pin as input
}

void loop() {
  digitalWrite(outputPin,HIGH);
  delay(1000);
  val = digitalRead(inputPin);   // read the input pin
  Serial1.print("Sent signal from: ");
  Serial1.println(outputPin);
  Serial1.print("Received signal: ");
  Serial1.println(val);
  delay(1);        // delay in between reads for stability
/*
  // reply only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    val = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(val, DEC);
  }
  */
}
