// Program written to take user input through the serial monitor 
// and allow the user to adjust the blink rate of the LED.
// @author pduncans
//@date 10/04/2021
//@version 1.0

int ledPin = 13;
int blinkOn = 1000;
int blinkOff = 1000;
int repeat = 1;

void setup() {
  //Setup the serial monitor with a baud rate of 9600
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  //Get the on time for the LED
  Serial.println("How many seconds should the light be on?");
  //Loop to wait for answer
  while(Serial.available()==0){
    //Loop just waits
  }
  blinkOn = Serial.parseInt();

  //Get the off time for the LED
  Serial.println("How many seconds should the light be off?");
  //Loop to wait for answer
  while(Serial.available()==0){
    //Loop just waits
  }
  blinkOff = Serial.parseInt();

  //Get number of times pattern should repeat
   Serial.println("How many times should this pattern repeat?");
  //Loop to wait for answer
  while(Serial.available()==0){
    //Loop just waits
  }
  repeat = Serial.parseInt();

  //Loop for pattern
  for (int i = 0; i < repeat; i++){
    //Set times for LED light
    digitalWrite(ledPin, HIGH);
    int on = blinkOn * 1000;
    delay(on);
    digitalWrite(ledPin, LOW);
    int off = blinkOff * 1000;
    delay(off);
  }
  Serial.println();
}
