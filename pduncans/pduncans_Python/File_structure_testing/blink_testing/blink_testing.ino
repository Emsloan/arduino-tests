// This sketch is used to quickly flash the DA-48's built in 
// LED light.  The light should blink on and off every 1/10th
// second if the sketch has been uploaded properly.

void setup() {
  // put your setup code here, to run once:
  pinMode(20, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(20, HIGH);
  delay(100);
  digitalWrite(20, LOW);
  delay(100);
  Serial.println("test");
}
