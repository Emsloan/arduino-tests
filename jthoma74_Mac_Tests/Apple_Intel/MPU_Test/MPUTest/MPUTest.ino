/*
 * MPUTest.ino
 * Description: Incomplete - Simple test sketch for MPU on GY-521
 * jthoma74 - 4/9/22
 */

#include <Wire.h>

//long gX, gY
long aX, aY

void setup() {
  Serial.begin(9600);
  Wire.begin();
  testMPU();
}

void testMPU() {
  Wire.beginTransmission(0b1101000);
  Wire.write(0x1C); 
  Wire.write(0b00000000); //accel configuration
  Wire.write(0x6B);
  Wire.write(0x00000000); //sleep register

  //gX = Wire.read()<<8|Wire.read();
  //gY = Wire.read()<<8|Wire.read();

  Wire.write(0x3B); //accel register
  Wire.requestFrom(0b1101000,6); 
  
  aX = Wire.read()<<8 | Wire.read();
  aY = Wire.read()<<8 | Wire.read();
  
  Serial.print("Accel X reading: ");
  Serial.print(aX);
  Serial.print("Accel Y reading: ");
  Serial.print(aY);

  Wire.endTransmission();
}
