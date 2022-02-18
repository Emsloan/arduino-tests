/* Sweep
  by BARRAGAN <http://barraganstudio.com>
  This example code is in the public domain.

  modified 8 Nov 2013
  by Scott Fitzgerald
  http://www.arduino.cc/en/Tutorial/Sweep
*/

// Task 225
// Servo sweep test with the AVR128DB48 is successful.
// Modifications made to default example to protect the servo and
// make pin hookup easier. pduncans

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
                      // Modified to run with pin 7 (PA7) on the DB48 pd
  myservo.attach(7);  // attaches the servo on pin 9 to the servo object
}

// Modified from 180 to 160,  to avoid overdriving the servo
// The extreme ends of the servo position can break the mechanism pduncans

void loop() {
  for (pos = 0; pos <= 160; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
