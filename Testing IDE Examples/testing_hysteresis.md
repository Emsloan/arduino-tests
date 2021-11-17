# Comparator - Hysteresis

### Example Code
```
/***********************************************************************|
| AVR DA/DB/DD analog comparator library                                |
|                                                                       |
| Hysteresis.ino                                                        |
|                                                                       |
| A library for interfacing with the AVR DA/DB analog comparator.       |
| Developed in 2019 by MCUdude                                          |
| https://github.com/MCUdude/                                           |
|                                                                       |
| In this example we use the negative input 2 and positive input 3 of   |
| the comparator. Those inputs were chosen so that any comparator could |
| be used in place of Comparator (Comparator0, AC0) and the comment     |
| would still be accurate.                                              |
| The output goes high if the positive input is higher than             |
| the negative input, and low otherwise. We'll also use the built-in    |
| hysteresis functionality to prevent false spikes.                     |
************************************************************************/

#include <Comparator.h>

void setup() {
  // Configure relevant comparator parameters
  Comparator.input_p = in_p::in0;      // Use positive input 0 - these are boring options, but they will compile everywhere
  Comparator.input_n = in_n::in0;      // Use negative input 0 - which is critical as these are used for CI testing too.
  Comparator.hysteresis = hyst::large; // Use a 50mV hysteresis
  Comparator.output = out::enable;     // Enable output on digital pin 7 (PA7)

  // Initialize comparator
  Comparator.init();

  // Start comparator
  Comparator.start();
}

void loop() {

}
```

### Result
Example failed to compile for board AVR DA-series 

### Error Messages
```

C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp: In member function 'void AnalogComparator::attachInterrupt(void (*)(), uint8_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:670:3: error: 'AC_INTMODE_NORMAL_t' was not declared in this scope
   AC_INTMODE_NORMAL_t intmode;
   ^~~~~~~~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:670:3: note: suggested alternative: 'AC_INTMODE_t'
   AC_INTMODE_NORMAL_t intmode;
   ^~~~~~~~~~~~~~~~~~~
   AC_INTMODE_t
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:674:7: error: 'intmode' was not declared in this scope
       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_POSEDGE_gc;
       ^~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:674:7: note: suggested alternative: 'pinMode'
       intmode = (AC_INTMODE_NORMAL_t)AC_INTMODE_NORMAL_POSEDGE_gc;
       ^~~~~~~
       pinMode
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:696:16: error: 'intmode' was not declared in this scope
   AC.INTCTRL = intmode | AC_CMP_bm;
                ^~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Comparator\src\Comparator.cpp:696:16: note: suggested alternative: 'pinMode'
   AC.INTCTRL = intmode | AC_CMP_bm;
                ^~~~~~~
                pinMode
exit status 1
Error compiling for board AVR DA-series.



```

### Possible Fixes and Notes
1.  AC_INTMODE_NORMAL_t intmode; is not declared within the scope of the program file, it is unable to compile and upload.  The decalration
does not exist within the Team 25 prototype core nor does it exist within the Dx Core from which the prototype is based upon.
The team must wait upon further updates before additional testing.




