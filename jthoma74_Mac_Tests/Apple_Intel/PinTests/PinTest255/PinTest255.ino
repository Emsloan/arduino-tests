#include <Servo.h>

/**
 * Testing pin maps using Analog read input on Arduino
 */

int outputPin = 11;  // pin to test
int inputPin = 7;    // input pin to read from output pin
int val = 0;      // store read value

void setup() {
  pinMode(ouputPin, OUTPUT);  // sets pin as output
  pinMode(inputPin, INPUT);    // sets pin as input
  serial3.begin(9600);
}

void loop() {
  digitalWrite(outputPin,HIGH);
  delay(1000)
  val = analogRead(inputPin);   // read the input pin
  Serial.println(buttonState);
  delay(1);        // delay in between reads for stability
}
