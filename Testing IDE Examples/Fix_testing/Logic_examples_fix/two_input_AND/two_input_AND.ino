/*************************************************
 * Two_input_AND
 *  
 * The purpose of this sketch is to create a two input 
 * AND gate for the AVR128DA48
 * 
 * 2-input AND truth table   
 * |PD0|PD1| Y |       
 * |---|---|---|           
 * | 0 | 0 | 0 |           
 * | 0 | 1 | 0 |           
 * | 1 | 0 | 0 |           
 * | 1 | 1 | 1 | 
 ************************************************/

//variables to store readings in
int input1;
int input2; 

//Output pin
int output_pin = 3; //can be set to any pin 

void setup() {
  //Set a pin to always on as a voltage source (PC6 or Pin 20)
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);

  //Write to serial
  Serial1.begin(9600);

  //Configure pins to gate inputs 
  pinMode(22, INPUT); // PD0
  pinMode(23, INPUT); // PD1
  

  //Configure output pin for gate
  pinMode(output_pin, OUTPUT); // PA3
} 

void loop() {
  //Read input pins voltages
  input1 = analogRead(22);
  input2 = analogRead(23);

  //Print values to serial monitor for 
  Serial1.print(input1);
  Serial1.print("    ");
  Serial1.println(input2);  
  
  // Configure logic gate 
  // Using 500 as a minimum to avoid partial voltages
  if(input1 > 500 && input2 > 500){
    digitalWrite(output_pin, HIGH);
  } else {
    digitalWrite(output_pin, LOW);
  }
}
