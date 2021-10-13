/*
  Sketch to blink the LED for 5 seconds on and 1 second off using 
  the AVR128DA48 arduino board.
  
  @author Paul Duncanson 
  @version 1.0
  @date 10/07/2021
*/

// LED is attached to pin 20 
// Must use the pin number because no bootloader was used to upload 
// the sketch.  A bootloader is needed to set the LED_BUILTIN pin 
// number

int LED = 20;

void setup() {
  // Initialize digital LED pin 20
    pinMode(LED, OUTPUT);
}


void loop() {
  // Loop for blinking the LED off and on
  digitalWrite(LED, HIGH);   
  delay(10000);              
  digitalWrite(LED, LOW); 
  delay(100);           
}
