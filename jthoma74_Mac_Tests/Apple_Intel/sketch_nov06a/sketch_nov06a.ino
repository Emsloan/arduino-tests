
int myNum;
String msg = "Testing serial monitor on Mac OS - Intel Chip";

 void setup() {
  pinMode(LED_BUILTIN,OUTPUT);
 
  /*set baud rate: */  
  Serial1.begin(57600);
}

void loop() {
  Serial1.println(msg);

  // passive loop to wait
  while(Serial1.available()==0){    
  }

  //Get number from user
  myNum = Serial1.parseInt();

  for (int i = 0; i < myNum; i++){
    digitalWrite(LED_BUILTIN,HIGH);
    delay(750);
    digitalWrite(LED_BUILTIN,LOW);
    delay(750);
  }
}
