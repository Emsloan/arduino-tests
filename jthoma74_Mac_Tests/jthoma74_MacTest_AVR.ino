/*
  Sketch to test AVR from MAC OS
  
  @author jthoma74 
  @version 1.0
  @date 11/2/21
*/

int LED = 20; 
int timer = 1000;

void setup() {
    // To run once:
    // Initialize LED
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
  digitalWrite(LED, LOW);
  delay(timer);
  digitalWrite(LED, HIGH);
  delay(timer);
  
  Serial.println("MAC Testing");
}
