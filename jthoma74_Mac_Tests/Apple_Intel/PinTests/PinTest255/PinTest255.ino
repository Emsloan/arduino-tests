#include <Servo.h>

/**
 * Testing pin maps using Analog read input on Arduino
 */

Servo serv;

void setup() {
  // put your setup code here, to run once:
  serv.attach(22); //analog read to test pin
  serial3.begin(9600);
  pinMode(4,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(4,HIGH);
  delay(1000);
  digitalWrite(4, LOW);
  delay(1000);

  analogRead(22); //read input passed back into analog input

}
