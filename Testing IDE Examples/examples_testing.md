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

### Possible Fixes
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
### Possible Fixes
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

