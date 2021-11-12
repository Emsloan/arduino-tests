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