/*
    MPU6050 Triple Axis Gyroscope & Accelerometer. Simple Accelerometer Example.
    Read more: http://www.jarzebski.pl/arduino/czujniki-i-sensory/3-osiowy-zyroskop-i-akcelerometr-mpu6050.html
    GIT: https://github.com/jarzebski/Arduino-MPU6050
    Web: http://www.jarzebski.pl
    (c) 2014 by Korneliusz Jarzebski
*/


//Modified by pduncans 04/08/2022

#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() 
{
  Serial3.begin(115200);

  Serial3.println("Initialize MPU6050");

  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    Serial3.println("Could not find a valid MPU6050 sensor, check wiring!");
    delay(500);
  }
}


void loop()
{
  Vector rawAccel = mpu.readRawAccel();
  Vector normAccel = mpu.readNormalizeAccel();

  Serial3.print(" Xraw = ");
  Serial3.print(rawAccel.XAxis);
  Serial3.print(" Yraw = ");
  Serial3.print(rawAccel.YAxis);
  Serial3.print(" Zraw = ");
  Serial3.println(rawAccel.ZAxis);
 
 // Slow down the scrolling for readability
  delay(1000);
}
