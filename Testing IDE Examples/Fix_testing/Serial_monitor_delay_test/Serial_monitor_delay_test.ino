/***********************************
Serial_monitor_delay_test

The purpose of this sketch is to attempt to slow down printing to the
serial monitor.  The issue stems from the AVR128DA48 board only printing
output inside the loop function.   

************************************/


void setup() {
  //Add a blinking light to assure sketch is functioning properly
  pinMode(LED_BUILTIN, OUTPUT);
  //Start the serial1 
  Serial1.begin(9600);
  //Insert Delay here
  //Wait for the serial port to connect before attempting to print
  while ( !Serial1 );
  //Print a line once to test if 
  Serial1.println("First print");
}



void loop() {
  //Blink the LED on and off with a 1 second delay
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  //Print every loop
  Serial1.println("Void loop print");
}
