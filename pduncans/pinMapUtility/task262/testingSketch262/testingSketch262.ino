// Task 264 testing pins 31-40 for the AVR128DB48

int testPin = 32;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(testPin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(testPin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(testPin, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
