/*
  Controlling a servo position using a potentiometer (variable resistor)
  by Michal Rinott <http://people.interaction-ivrea.it/m.rinott>

  modified on 8 Nov 2013
  by Scott Fitzgerald
  http://www.arduino.cc/en/Tutorial/Knob
*/

// Test passed 

// Modified due to a broken potentiometer 
// Now works with no potentiometer but tests
// the functions contained in the Servo.h header file

#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int potpin = A7;  // analog pin used to connect the potentiometer - analog channel 7 exists everywhere!
int val = 0;    // variable to read the value from the analog pin

void setup() {
  //Modified: Pin 9 is not an anolog pin on the DB48, moved to PD0 (22)
  myservo.attach(22);  // attaches the servo on pin 9 to the servo object
  //Added to monitor the potentiometer readings and values sent to functions
  Serial3.begin(9600);
}

void loop() {
  //Commented out to remove the need for a potentiometer knob
  //val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  
  
  val = map(val, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)

  //Output value of val
  Serial3.println(val);
  
  myservo.write(val);                  // sets the servo position according to the scaled value

  //Original delay was set to 15ms, which is too short for the servo's spin to be observed
  delay(1000);                           // waits for the servo to get there
  
  //Change the values of val to a random number (0 to 1022)
  val = random(1023); 
  //Output the new value
  Serial3.print("Changed val to  ");
  Serial3.println(val);
  
}
