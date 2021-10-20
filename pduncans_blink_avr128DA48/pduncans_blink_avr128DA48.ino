/*
  Sketch to verify that the serial monitor is functioning properly on  
  the AVR128DA48 arduino board.
  
  @author Paul Duncanson 
  @version 1.0
  @date 10/18/2021
*/


int LED = 20; //built in LED is on pin
int timer = 100;

void setup() {
  // Initialize digital LED pin 20
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}


void loop() {
  digitalWrite(LED, LOW);
  delay(timer);
  digitalWrite(LED, HIGH);
  delay(timer);
  
  Serial.println("testing");
  

}
