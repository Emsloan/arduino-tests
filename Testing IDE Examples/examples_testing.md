# Comparator - Simple_comparator

### Example Code
```
/***********************************************************************|
| AVR DA/DB analog comparator library                                   |
|                                                                       |
| Simple_comparator.ino                                                 |
|                                                                       |
| A library for interfacing with the AVR DA/DB analog comparator.       |
| Developed in 2019 by MCUdude                                          |
| https://github.com/MCUdude/                                           |
|                                                                       |
| In this example we use the negative and positive input 0 of the       |
| comparator. The output goes high if the positive input is higher than |
| the negative input, and low otherwise.                                |
|***********************************************************************/

#include <Comparator.h>

void setup() {
  // Configure relevant comparator parameters
  Comparator.input_p = in_p::in0;  // Use positive input 0 (PD2)
  Comparator.input_n = in_n::in0;  // Use negative input 0 (PD3)
  Comparator.output = out::enable; // Enable output on digital pin 7 (PA7)

  // Initialize comparator
  Comparator.init();

  // Start comparator
  Comparator.start();
}

void loop() {

}
```

### Result
Example failed to compile

### Error Message
```
Arduino: 1.8.16 (Windows 10), Board: "AVR DA-series, AVR128DA48"

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:134:6: error: prototype for 'void AnalogComparator::stop()' does not match any in class 'AnalogComparator'

 void AnalogComparator::stop() {

      ^~~~~~~~~~~~~~~~

In file included from C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:1:0:

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.h:90:10: error: candidate is: void AnalogComparator::stop(bool)

     void stop(bool restorepins = false);

          ^~~~

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp: In member function 'void AnalogComparator::attachInterrupt(void (*)(), uint8_t)':

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:139:3: error: 'AC_INTMODE_NORMAL_t' was not declared in this scope

   AC_INTMODE_NORMAL_t intmode;

   ^~~~~~~~~~~~~~~~~~~

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:139:3: note: suggested alternative: 'AC_INTMODE_t'

   AC_INTMODE_NORMAL_t intmode;

   ^~~~~~~~~~~~~~~~~~~

   AC_INTMODE_t

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:143:7: error: 'intmode' was not declared in this scope

       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_POSEDGE_gc;

       ^~~~~~~

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:143:7: note: suggested alternative: 'pinMode'

       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_POSEDGE_gc;

       ^~~~~~~

       pinMode

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:160:16: error: 'intmode' was not declared in this scope

   AC.INTCTRL = intmode | AC_CMP_bm;

                ^~~~~~~

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:160:16: note: suggested alternative: 'pinMode'

   AC.INTCTRL = intmode | AC_CMP_bm;

                ^~~~~~~

                pinMode

exit status 1

Error compiling for board AVR DA-series.



This report would have more information with
"Show verbose output during compilation"
option enabled in File -> Preferences.

```

### Ideas
1. Add a declaration for "void stop()" in Comparator.h file.  It appears there is no declaration for this function.
2. Find location of missing "AC_INTMODE_NORMAL_t" enum declaration or add a new one. 

```
Search "AC_INTMODE_NORMAL_t" (1 hit in 1 file of 439 searched)
  C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\DxCore\keywords.txt (1 hit)
	Line 278: AC_INTMODE_NORMAL_t	LITERAL1
```
A search performed only found one mention of the "AC_INTMODE_NORMAL_t".  It is contained in the keywords.txt file and is not attached
to any coding within the core.


# Comparator - Interrupt
### Example Code
```
/***********************************************************************|
| AVR DA/DB analog comparator library                                   |
|                                                                       |
| Interrupt.ino                                                         |
|                                                                       |
| A library for interfacing with the AVR DA/DB analog comparator.       |
| Developed in 2019 by MCUdude                                          |
| https://github.com/MCUdude/                                           |
|                                                                       |
| In this example we use an internal reference voltage instead of an    |
| external one on the negative pin. This eliminates the need for an     |
| external voltage divider to generate a reference. Note that the       |
| internal reference requires a stable voltage to function properly.    |
| Instead of using a physical output pin we're instead triggering an    |
| interrupt that will run a user defined function.                      |
|                                                                       |
| This is the formula for the generated voltage:                        |
| Vdacref = (DACREF / 256) * Vref                                       |
|***********************************************************************/

#include <Comparator.h>
/* This flag will be set true by the interrupt. Since it's modified in
 * an interrupt but read outside of that interrupt, it must be volatile.
 */
volatile bool int_fired = 0;

void setup() {
  // Configure serial port
  Serial.begin(115200);

  // Configure relevant comparator parameters
  Comparator.input_p = in_p::in0;       // Use positive input 0 (PD2)
  Comparator.input_n = in_n::dacref;    // Connect the negative pin to the DACREF voltage
  Comparator.reference = ref::vref_2v5; // Set the DACREF voltage to 2.5V
  Comparator.dacref = 255;              // Gives us 2.5V -> (255 / 256) * 2.5V = 2.5V
  Comparator.hysteresis = hyst::large;  // Use a 50mV hysteresis
  Comparator.output = out::disable;     // Use interrupt trigger instead of output pin

  // Initialize comparator
  Comparator.init();

  // Set interrupt (supports RISING, FALLING and CHANGE)
  Comparator.attachInterrupt(interruptFunction, RISING);

  // Start comparator
  Comparator.start();
}

void loop() {
  if (int_fired) { // Check our flag here
    Serial.println("Output of analog comparator went high!");
    int_fired = 0; // clear our flag so we don't sit there spamming the serial port
  }
}

// This function runs when an interrupt occurs
void interruptFunction() {
  /* You might want to do this, but no! Do not do this!
  Serial.println("Output of analog comparator went high!");
  * Avoid printing to serial within an ISR. The print functions can potentially block for,
  * in the worst case (tx buffer full when print is started), as long as the entire string
  * takes to print (calculated as characters divided by baud/10 - each byte is sent as
  * 10 bits, because there's a start and stop bit. At best, this would cause millis to lose
  * time, and at worst block other critical functions. If you really need to, printing a
  * single character is much less of a hazard than a longer message, and is acceptable for
  * debugging purposes (though still undesirable), as that both reduces the worst case
  * execution time and reduces the chance of there being any blocking delay- only a completely
  * full TX buffer would cause it. This also makes it harder for the interrupt to fire so
  * frequently that the messages it tries to print will outrun the serial port - which is the
  * nightmare scenario.
  * The correct approach is what we demonstrate - set a flag that you can check on the
  * next pass through loop.
  */
  int_fired = 1; // This can be kept short and fast,
}
```
### Result
Example failed to compile

### Error Message
```
Arduino: 1.8.16 (Windows 10), Board: "AVR DA-series, AVR128DA48"

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp: In member function 'void AnalogComparator::attachInterrupt(void (*)(), uint8_t)':

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:670:3: error: 'AC_INTMODE_NORMAL_t' was not declared in this scope

   AC_INTMODE_NORMAL_t intmode;

   ^~~~~~~~~~~~~~~~~~~

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:670:3: note: suggested alternative: 'AC_INTMODE_t'

   AC_INTMODE_NORMAL_t intmode;

   ^~~~~~~~~~~~~~~~~~~

   AC_INTMODE_t

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:674:7: error: 'intmode' was not declared in this scope

       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_POSEDGE_gc;

       ^~~~~~~

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:674:7: note: suggested alternative: 'pinMode'

       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_POSEDGE_gc;

       ^~~~~~~

       pinMode

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:696:16: error: 'intmode' was not declared in this scope

   AC.INTCTRL = intmode | AC_CMP_bm;

                ^~~~~~~

C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:696:16: note: suggested alternative: 'pinMode'

   AC.INTCTRL = intmode | AC_CMP_bm;

                ^~~~~~~

                pinMode

exit status 1

Error compiling for board AVR DA-series.
```
### Ideas
1. The error message points to the same missing type as the Comparator - Simple_comparator.  This type is not declared anywhere in our 
core's package and doesn't appear in the original DxCore either.  It must be added or the example must be modified.

#### Search of Team 25's package
```
Search "AC_INTMODE_NORMAL_t" (5 hits in 2 files of 465 searched)
  C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp (4 hits)
	Line 670:   AC_INTMODE_NORMAL_t intmode;
	Line 674:       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_POSEDGE_gc;
	Line 677:       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_NEGEDGE_gc;
	Line 680:       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_BOTHEDGE_gc;
  C:\Users\paulm\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\DxCore\keywords.txt (1 hit)
	Line 278: AC_INTMODE_NORMAL_t	LITERAL1
```
#### Search of current DxCore
```
Search "AC_INTMODE_NORMAL_t" (5 hits in 2 files of 613 searched)
  D:\Homework\Capstone\DXCore\DxCore\megaavr\libraries\Comparator\src\Comparator.cpp (4 hits)
	Line 670:   AC_INTMODE_NORMAL_t intmode;
	Line 674:       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_POSEDGE_gc;
	Line 677:       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_NEGEDGE_gc;
	Line 680:       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_BOTHEDGE_gc;
  D:\Homework\Capstone\DXCore\DxCore\megaavr\libraries\DxCore\keywords.txt (1 hit)
	Line 278: AC_INTMODE_NORMAL_t	LITERAL1
```

# EEPROM - eeprom_clear
### Example Code
```
/*
 * EEPROM Clear
 *
 * Sets all of the bytes of the EEPROM to 0xFF (blank).
 * Please see eeprom_iteration for a more in depth
 * look at how to traverse the EEPROM.
 *
 * This example code is in the public domain.
 */

#include <EEPROM.h>

void setup() {
  // initialize the LED pin as an output.
  pinMode(20, OUTPUT);

  /*
   * Iterate through each byte of the EEPROM storage.

   * Larger AVR processors have larger EEPROM sizes, E.g:
   * tinyAVR 0/1/2-series 2k flash:      64b
   * tinyAVR 0/1/2-series 4-8k flash:    128b
   * tinyAVR 0/1/2-series 16-32k flash:  256b
   * megaAVR 0-series:                   256b (all flash sizes)
   * DA, DB, EA-series:                  512b (all flash sizes)
   * DD-series:                          256b (all flash sizes)

   * Rather than hard-coding the length, you should use the pre-provided length function.
   * This will make your code portable to all AVR processors.
   */

  for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0xFF);
  }

  // turn the LED on when we're done
  digitalWrite(20, HIGH);
}

void loop() {
  /* Empty loop.  */
}
```
Note: Code slightly modified to utilize the built in LED on pin 20.  

### Result
Example compiled and behaved correctly.  

# EEPROM - eeprom_crc
### Example Code
```
/* CRC eeprom validation example
 *
 * Written by Christopher Andrews.
 * CRC algorithm generated by pycrc, MIT licence ( https://github.com/tpircher/pycrc ).
 *
 * A CRC is a simple way of checking whether data has changed or become corrupted.
 * This example calculates a CRC value directly on the EEPROM values.
 * The purpose of this example is to highlight how the EEPROM object can be used just like an array.
 *
 * As well as, apparently demonstrating a CRC implementation instead of using the
 * builtin library from avr-libc "util/crc16.h"?
 * 16-bit CRC is probably a better match for the resources of an AVR, and
 * that implementation was done in assembly and is lightning fast.
 * This one is - maybe not even a sound implementation of a CRC algorithm...
 * Those rightshifts don't roll anything over, while every other CRC implementation
 * I've looked at does.  -Spence Konde 2021
 */

#include <Arduino.h>
#include <EEPROM.h>

void setup() {

  //Start serial
  Serial.begin(115200);

  //Print length of data to run CRC on.
  Serial.print("EEPROM length: ");
  Serial.println(EEPROM.length());

  //Print the result of calling eeprom_crc()
  Serial.print("CRC32 of EEPROM data: 0x");
  Serial.println(eeprom_crc(), HEX);
  Serial.print("\n\nDone!");
}

void loop() {
  /* Empty loop */
}

unsigned long eeprom_crc(void) {

  const unsigned long crc_table[16] = {
    0x00000000, 0x1db71064, 0x3b6e20c8, 0x26d930ac,
    0x76dc4190, 0x6b6b51f4, 0x4db26158, 0x5005713c,
    0xedb88320, 0xf00f9344, 0xd6d6a3e8, 0xcb61b38c,
    0x9b64c2b0, 0x86d3d2d4, 0xa00ae278, 0xbdbdf21c
  };

  unsigned long crc = ~0L;

  for (int index = 0 ; index < EEPROM.length()  ; ++index) {
    crc = crc_table[(crc ^ EEPROM[index]) & 0x0f] ^ (crc >> 4);
    crc = crc_table[(crc ^ (EEPROM[index] >> 4)) & 0x0f] ^ (crc >> 4);
    crc = ~crc;
  }
  return crc;
}
```

### Result
Code compiles correctly, but the serial monitor displays nothing.

### Ideas
1. Changing the "Serial" variable to "Serial1", which works in other sketches, has no effect on the serial monitor's output.   

# EEPROM - eeprom_get

### Sample Code
```
/* eeprom_get example.
 *
 * This shows how to use the EEPROM.get() method.
 *
 * To pre-set the EEPROM data, run the example sketch eeprom_put.
 * This sketch will run without it, however, the values shown
 * will be shown from what ever is already on the EEPROM.
 *
 * This may cause the serial object to print out a large string
 * of garbage if there is no null character inside one of the strings
 * loaded.
 *
 * Written by Christopher Andrews 2015
 * Released under MIT licence.
 */

#include <EEPROM.h>

void setup() {

  float f = 0.00f;   //Variable to store data read from EEPROM.
  int eeAddress = 0; //EEPROM address to start reading from

  Serial.begin(115200);

  Serial.print("Read float from EEPROM: ");

  //Get the float data from the EEPROM at position 'eeAddress'
  EEPROM.get(eeAddress, f);
  Serial.println(f, 3);    //This may print 'ovf, nan' if the data inside the EEPROM is not a valid float.

  /*
   * As get also returns a reference to 'f', you can use it inline.
   * E.g: Serial.print( EEPROM.get( eeAddress, f ) );
   */

  /*
   * Get can be used with custom structures too.
   * I have separated this into an extra function.
   */

  secondTest(); //Run the next test.
}

struct MyObject {
  float field1;
  byte field2;
  char name[10];
};

void secondTest() {
  int eeAddress = sizeof(float); //Move address to the next byte after float 'f'.

  MyObject customVar; //Variable to store custom object read from EEPROM.
  EEPROM.get(eeAddress, customVar);

  Serial.println("Read custom object from EEPROM: ");
  Serial.println(customVar.field1);
  Serial.println(customVar.field2);
  Serial.println(customVar.name);
}

void loop() {
  /* Empty loop  */
}
```

### Result
Code compiles correctly, but the serial monitor displays nothing.

### Ideas
1. Changing the code to "Serial1" has no effect on the output of this example.  
2. It appears that the serial monitor will only output data when a print function call is
placed in the void loop() and the variable is set to "Serial1".   
3. We need to figure out why the placement of print function calls affects the output to the serial monitor. 

### Example of Findings
```
void secondTest() {
  int eeAddress = sizeof(float); //Move address to the next byte after float 'f'.

  MyObject customVar; //Variable to store custom object read from EEPROM.
  EEPROM.get(eeAddress, customVar);

  Serial1.println("Read custom object from EEPROM: ");
  Serial1.println(customVar.field1);
  Serial1.println(customVar.field2);
  Serial1.println(customVar.name);
}

void loop() {
  /* Empty loop  */
  Serial1.println("Read float from EEPROM: "); //Adding this line and changing to "Serial1" will print to serial monitor
}
```

# EEPROM - Iteration
### Sample Code
```
/* eeprom_iteration example.
 *
 * A set of example snippets highlighting the
 * simplest methods for traversing the EEPROM.
 *
 * Running this sketch is not necessary, this is
 * simply highlighting certain programming methods.
 *
 * Written by Christopher Andrews 2015
 * Released under MIT licence.
 */

#include <EEPROM.h>

void setup() {

  /*
   * Iterate the EEPROM using a for loop.
   */

  for (int index = 0 ; index < EEPROM.length() ; index++) {

    //Add one to each cell in the EEPROM
    EEPROM[ index ] += 1;
  }

  /*
   * Iterate the EEPROM using a while loop.
   */

  int index = 0;

  while (index < EEPROM.length()) {

    //Add one to each cell in the EEPROM
    EEPROM[ index ] += 1;
    index++;
  }

  /*
   * Iterate the EEPROM using a do-while loop.
   */

  int idx = 0;  //Used 'idx' to avoid name conflict with 'index' above.

  do {

    //Add one to each cell in the EEPROM
    EEPROM[ idx ] += 1;
    idx++;
  } while (idx < EEPROM.length());


} //End of setup function.

void loop() {}
```

### Result
Code compiles correctly and appears to function properly.

# EEPROM - eeprom_put
### Sample Code
```
/* eeprom_put example.
 *
 * This shows how to use the EEPROM.put() method.
 * Also, this sketch will pre-set the EEPROM data for the
 * example sketch eeprom_get.
 *
 * Note, unlike the single byte version EEPROM.write(),
 * the put method will use update semantics. As in a byte
 * will only be written to the EEPROM if the data is actually
 * different in order to avoid unnecessary write/erase cycles.
 *
 * Written by Christopher Andrews 2015
 * Released under MIT licence.
 */

#include <EEPROM.h>

struct MyObject {
  float field1;
  byte field2;
  char name[10];
};

void setup() {

  Serial.begin(115200);

  float f = 123.456f;  //Variable to store in EEPROM.
  int eeAddress = 0;   //Location we want the data to be put.


  // One simple call, with the address first and the object second.
  EEPROM.put(eeAddress, f);

  Serial.println("Written float data type!");

  /* Put is designed for use with custom structures also. */

  //Data to store.
  MyObject customVar = {
    3.14f,
    65,
    "Working!"
  };

  eeAddress += sizeof(float); //Move address to the next byte after float 'f'.

  EEPROM.put(eeAddress, customVar);
  Serial.print("Written custom data type! \n\nView the example sketch eeprom_get to see how you can retrieve the values!");
}

void loop() {
  /* Empty loop */
}
```
### Result
Code compiles correctly, but the serial monitor displays nothing.

### Ideas
1. Serial1 works to print to the serial monitor but only if it is placed in the continuous loop.

```
void loop() {
  /* Empty loop */
  Serial1.println("Test");
}
```

![Alt text](pics/serial_test.png "Testing serial")

# EEPROM - eeprom_read

### Sample Code
```
/* EEPROM Read
 *
 * Reads the value of each byte of the EEPROM and prints it
 * to the computer.
 * This example code is in the public domain.
 */

#include <EEPROM.h>

// start reading from the first byte (address 0) of the EEPROM
int address = 0;
byte value;

void setup() {
  Serial.begin(115200);
}

void loop() {
  // read a byte from the current address of the EEPROM
  value = EEPROM.read(address);

  Serial.print(address);
  Serial.print("\t");
  Serial.print(value, DEC);
  Serial.println();

  /*
   * Iterate through each byte of the EEPROM storage.

   * Larger AVR processors have larger EEPROM sizes, E.g:
   * tinyAVR 0/1/2-series 2k flash:      64b
   * tinyAVR 0/1/2-series 4-8k flash:    128b
   * tinyAVR 0/1/2-series 16-32k flash:  256b
   * megaAVR 0-series:                   256b (all flash sizes)
   * DA, DB, EA-series:                  512b (all flash sizes)
   * DD-series:                          256b (all flash sizes)

   * Rather than hard-coding the length, you should use the pre-provided length function.
   * This will make your code portable to all AVR processors.
   */

  address = address + 1;
  if (address == EEPROM.length()) {
    address = 0;
  }

  /*
   * As the EEPROM sizes are powers of two, wrapping (preventing overflow) of an
   * EEPROM address is also doable by a bitwise and of the length - 1.

   * ++address &= EEPROM.length() - 1;
   */

  delay(500);
}
```
### Result
Code compiles correctly and output is printed to the serial monitor.  This occurs only when 'Serial'
is changed to 'Serial1'.

![Alt text](pics/eeprom_read.png "EEPROM read")

# DxCore - EnhancedIODemo
### Sample Code
```
/*********************\\*****************************//************************
                       \\   Enhanced I/O API Demo   //
                        ^^-------------------------^^

The hardware in modern AVR devices (Dx, tinyAVR 0/1/2, mega 0-series) is more
sophisticated than that which was featured in previous AVR products. This core
provides a few simple I/O functions to take advantage of the new pin I/O
capabilities. This file demonstrates their function and calling conventions in
brief.

In these examples, we pick a pin that we know the part has -PIN_PA2 on tinyAVR
and PIN_PD4 for everything else - all ATtiny have PA0~PA3, PA6,and PA7; PA0 is
generally not available as it's used for UPDI.

Now, we could have also used PIN_PA1 - that works on all parts, except that on
the DD and DB-series, that pin may be used for a crystal, making it ill-suited
for use in a demonstration.

This sketch isn't meant to be used as is - it's more of a starting point, or
resource to cooy+paste starting points from.

******************************************************************************/

#if defined (MEGATINYCORE)
  #define DEMO_PIN PIN_PA2
  #define DEMO_PIN2 PIN_PA3
#else
  #define DEMO_PIN PIN_PD4
  #define DEMO_PIN2 PIN_PD5

#endif

void setup() {


}


void loop() {
  openDrainBitbang(0x0DF0AD8B); //or, with human endianness, 0x8BADF00D
}

/*-----------------------------------------------------------------------------
openDrain(pin,value) and openDrainFast(pin,value)

Nothing specific to the modernAVRs about openDrain() - it's the "missing"
digital I/O function. To get pullup, set it INPUT_PULLUP with pinMode first, then
call openDrain() - remember that, emulating the behavior of classic AVRs, the
core configures pins as inputs unless told otherwise.
  Usage:
    openDrain(DEMO_PIN, LOW);
    openDrain(DEMO_PIN, FLOATING);
    openDrain(DEMO_PIN, CHANGE);
    openDrainFast(DEMO_PIN, LOW);
    openDrainFast(DEMO_PIN, FLOATING);
    openDrainFast(DEMO_PIN, CHANGE);

  LOW sets pin mode to OUTPUT.
  FLOATING sets pin mode to INPUT. If there is a pullup
enabled or external pullup connected, the pin will be pulled up assuming
nothing else connected to it is driving the pin LOW; otherwise the pin will
float.
  CHANGE toggles the direction.

  Like all Fast I/O functions, you must pass a constant pin and you should try
  to pass a constant value as well. The function when both are constant, and
  the value is not CHANGE optimizes to a single cbi or sbi instruction, occupying
  2 bytes of flash and executing within a single clock cycle. This function is
  ((always_inline)) - but with a single 2 byte instruction, this is always
  more efficient. When the value is CHANGE, it uses two instructions, one a
  double-size STS instruction, for 6 bytes and 3 clock cycles.

-----------------------------------------------------------------------------*/

void openDrainBitbang(uint32_t data) {
  pinMode(DEMO_PIN, INPUT_PULLUP);
  pinMode(DEMO_PIN2, INPUT_PULLUP);
  openDrain(DEMO_PIN, FLOATING);
  openDrain(DEMO_PIN2, FLOATING);
  // Now both pins are open drains with their pullup enabled
  // now they use one as a clock, and the other as data in some sort of digital
  // communication scheme waiting to make sure the pins come back to HIGH like
  // I2C does.
  // When it's not waiting for the pins to rise back to HIGH, the code runs
  for (uint8_t i = 0; i < 32; i++) {
    while (digitalReadFast(DEMO_PIN) != HIGH || digitalReadFast(DEMO_PIN2) != HIGH);
    //Wait for them to be pulled high - probably won't loop, but maybe high capacitance on
    //the lines or weak pullups, or other device holding low (like I2C clock stretching)
    _NOPNOP(); // wait four clocks so the receiver has a chance to see the same thing as we did; We could even wait longer here
    _NOPNOP();
    if (((uint8_t)data) & 0x01) {
      openDrainFast(DEMO_PIN2, LOW); ///set up data line - this likely compiles to cbi, sbrc, sbi
      // (certainly that's what you;'d expect the compiler to to do, but sometimes it's not so smart)
    }
    _NOPNOP(); // wait four clocks so the receiver has a chance to see the same thing as we did; We could even wait longer here
    _NOPNOP();
    openDrainFast(DEMO_PIN, LOW);
    data >>= 1;  //if we'd immediately released it, it would only be low for a fraction of a microsecond.
    // doing that math in there is liks a quarter microsecond delay.
    openDrainFast(DEMO_PIN, FLOATING);
    openDrainFast(DEMO_PIN2, FLOATING);
    //release pins.
  }

}
```
### Result
Code compiles correctly

# DxCore - ModernRevSer
### Code Sample

```
/* Read the silicon revision of a "modern" (post-2016, AVRxt) part, including megaAVR 0-series,
 * tinyAVR 0/1/2-series, AVR Dx-series, and likely the upcoming AVR Ex-series.
 * classic AVRs do not have a uniform serial number scheme like the new ones do. Some have one
 * located in the sigrow, others do not.
 * Also reads out the fuses and serial number. The fuses and serial number were part of an
 * attempt to determine whether the date code was embedded into the serial number somehow.
 * I suspect it is possible to determine the date code from it in some way.
 * A few interesting things to note about the serial number:
 *    The data bytes do not appear to use the full range of values - for
 *        most bytes, if you print each byte as hex, you get 2 decimal
 *        digits, that is, it's BCD.
 *    What little entropy it provides entropy is not distributed uniformly
 *        across the serial number. That is to say, it's a serial number,
 *        not a hash of a serial number. Don't count on it being impossible
 *        to guess the serial number.
 *    For these reasons, it is possible that additional information can be deduced from it
 *    In fact, on the Dx-series, the IO header identifies the meaning of each byte! Based on the similarity
 *    of the values observed in the wild, it is likely that the numbering scheme is similar for other parts.
 *  LOTNUM0:LOTNUM1:LOTNUM2:LOTNUM3:LOTNUM4:LOTNUM5  6 bytes of lot number
 *  RANDOM :SCRIBE : XPOS0 : XPOS1 : YPOS0 : YPOS1   1 random, unsure what "scribe" is, and 2 bytes each for X and Y position of die on wafer
 *   RES0  : RES1  : RES2  : RES3                    4 "reserved" bytes
 */


#if (__AVR_ARCH__ < 100)
  #error "This sketch is designed for 'modern AVR' parts only (post-2016, when they revised peripherals and instruction set timing)"
#endif
void setup() {
  Serial.begin(115200);
  Serial.println();
  delay(1000);
  Serial.print("REVID: ");
  #ifdef SIGROW_SERNUM15 //AVR Dx-series= - different format
  char major = 0x40 + (SYSCFG.REVID >> 4);
  Serial.print(major);
  Serial.println(SYSCFG.REVID & 0x0F);
  #else
  Serial.println('@' + SYSCFG.REVID);
  #endif
  Serial.print("S/N: ");
  volatile uint8_t *mptr = &SIGROW_SERNUM0;
  showHex(*mptr++);
  for (byte i = 0; i < 15; i++) {
    Serial.print(':');
    showHex(*mptr++);
  }
  Serial.println();
  Serial.print("FUSES: ");
  mptr = FUSES_START;
  showHex(*mptr++);
  for (byte i = 1; i < 9; i++) {
    Serial.print(':');
    showHex(*mptr++);
  }
  Serial.println();
}

void showHex(const byte b) {
  char x = (b >> 4) | '0';
  if (x > '9') {
    x += 7;
  }
  Serial.write(x);
  x = (b & 0x0F) | '0';
  if (x > '9') {
    x += 7;
  }
  Serial.write(x);
}

void loop() {
  // put your main code here, to run repeatedly:

}
```
### Result
Code compiles correctly and output is printed to the serial monitor.  This occurs only when serial
is set to 'Serial1'.

### Ideas
1.  Moving the "major" variable into the void loop() function will print the value stored in the char variable.

![Alt text](pics/moderncode.png "ModernRevSer")

![Alt text](pics/modernrevser.png "ModernRevSer")

# DxCore - SAMPLENDemo

### Sample code
```
/*
ADC0.SAMPCTRL demo

Connect a 1 MEG resistor between PD1 and PD0.

This makes PD0 a very high impedance input, controlled by PD1.
This sketch flips PD1 and then immediately takes some readings on PD0, printing the first one.
Format output is conducive to graphing in excel/etc (save as .csv)
One thing that is important to remember is that what matters is what the last voltage READ BY the ADC was.
For example, if you switch back and forth between reading a high impedance source, and a voltage very close to ground,
your numbers will err low with a low SAMPLEN, while if you were last measuring a high voltage, if would err high.
This of course means that if you are continually measuring the same high impedance, but slow changing voltage, you can
afford to use a shorter sample length than if you were switching between multiple analog voltages.

And finally, notice how it is slower when the change is from low to high vs high to low - which strikes me as
rather odd. Also that it goes all the way to 0 on a LOW, but not all the way to 4095 on a HIGH.


*/

void setup() {
  pinMode(PIN_PD1, OUTPUT);
  digitalWrite(PIN_PD1, 0);
  ADC0.SAMPCTRL = 0xFF;
  analogReadResolution(12);
  Serial.begin(1000000);
  delay(1000);
  analogRead(PIN_PD0);
}

void loop() {
  ADC0.SAMPCTRL++;
  digitalWrite(PIN_PD1, 1);
  Serial.print(analogRead(PIN_PD0));
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  Serial.print(",");
  digitalWrite(PIN_PD1, 0);
  Serial.println(analogRead(PIN_PD0));
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  analogRead(PIN_PD0);
  if (ADC0.SAMPCTRL == 255) {
    while (1);
  }
}
```

### Result
Code compiles correctly and output is printed to the serial monitor.  This occurs only when 'Serial'
is set to 'Serial1'.