//Simple program to Blink the Nano Every LED light on for 5 seconds and off for 1 second
//Set pin for LED light
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  //Turn on LED
  digitalWrite(ledPin, HIGH);
  delay(5000);
  //Turn off LED
  digitalWrite(ledPin, LOW);
  delay(1000);
}
