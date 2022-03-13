// Task 266 testing pins 51-56 for the AVR128DB48

int testPin = A21;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(testPin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(testPin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);                       // wait for a second
  digitalWrite(testPin, LOW);    // turn the LED off by making the voltage LOW
  delay(100);                       // wait for a second
}
