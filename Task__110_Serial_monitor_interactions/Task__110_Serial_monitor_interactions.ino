/*
 * Serial Monitor communications with the avr128DA48 can be accomplished
 * by using "Serial1" instead of the defualt "Serial".  The default "Serial"
 * is the common way of communication through the serial monitor, but it doesn't work  
 * with the current Team 25 package.  Fixing this issue should be a task added 
 * to a future sprint.  
 * 
 * Note: The first time through the loop() the message is not displayed until the
 * user enters a number into the serial monitor.  Future iterations display the  
 * message properly.
 */

int myNum;
String msg = "Give me a number:";
 
 void setup() {
  pinMode(LED_BUILTIN,OUTPUT);  
  Serial1.begin(57600);
}

void loop() {
  Serial1.println(msg);
  //Loop to wait for 
  while(Serial1.available()==0){    
  }

  //Get number from user
  myNum = Serial1.parseInt();
  
  for (int i = 0; i < myNum; i++){
    digitalWrite(LED_BUILTIN,HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN,LOW);
    delay(500);
  }
}
