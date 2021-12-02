# Summary: IDE Example Tests 
| Example							| Compiles	| Notes													|
|-----------------------------------|:---------:|-------------------------------------------------------|
| Flash - FlashDemo 				| No		| Fix: Enable writing to flash in Boards.txt    		|
| Comparator - Hysteresis			| No		| AC_INTMODE_NORMAL_t type doesn't exist in the core	|
| Comparator - internal_reference	| No 		| AC_INTMODE_NORMAL_t type doesn't exist in the core	|
| Comparator - Simple_comparator	| No		| AC_INTMODE_NORMAL_t type doesn't exist in the core	|
| Comparator - Interrupt			| No		| AC_INTMODE_NORMAL_t type doesn't exist in the core	|
| EEPROM - eeprom_clear				| Yes		| None													|
| EEPROM - eeprom_crc				| Yes		| "Serial1" only prints in the "void loop()" function	|
| EEPROM - eeprom_get				| Yes		| "Serial1" only prints in the "void loop()" function	|
| EEPROM - Iteration				| Yes		| None													|
| EEPROM - eeprom_put				| Yes		| 'Serial1' only prints in the "void loop()" function	|
| EEPROM - eeprom_read				| Yes		| Must change "Serial" to 'Serial1'						|
| DxCore - EnhancedIODemo			| Yes		| None													|
| DxCore - ModernRevSer				| Yes		| 'Serial1' only prints in the 'void loop()' function	|
| DxCore - SAMPLENDemo				| Yes		| 'Serial1' only prints in the 'void loop()' function	|
| Logic - Three_input_AND			| Yes		| AND remains off regardless of input status			|
| Logic - Three_input_NAND			| Yes		| NAND remains on regardless of input status			|
| Logic - Three_input_OR			| Yes		| OR gate remains on regardless of input status			|
| Logic - Two_input_AND				| Yes		| AND remains on regardless of the input status			|
| Logic - Two_input_NAND			| Yes		| NAND output remains off regardless of input status	|
| Logic - Two_input_OR				| Yes		| OR gate's ouput remains on regardless of input status	|
| Logic - Modulate					| No		| tcb1 is currently not setup							|
| Logic - Oscillate					| No		| tca0_cnta is currently not setup						|
| Logic - TCDThirdPWM				| No		| Issue	in Event.h										|
| Logic - Five_input_NOR			| Yes		| None													|
| Logic - Interrupt					| Yes		| None													|
| Logic - LatchNoSeq				| Yes		| None													|
| Opamp - Inverting_amplifier		| No		| 'Opamp0' object is not defined when running			|
| Opamp - Inverting_amplifier_with_follower| No | 'Opampx' objects are undefined						|
| Opamp - Non_inverting_amplifier	| No		| init() function doesn't setup variables properly		|
| Opamp - Voltage_follower			| No 		| init() function doesn't setup variables properly		|
| Servo_DxCore - Knob				| Yes		| None													|
| Servo_DxCore - ServoMaxTest		| Yes		| None													|
| Servo_DxCore - Sweep				| Yes		| None													|
| Servo - Knob						| Yes		| A servo is required to fully test this example		|
| Servo - ServoMaxTest				| Yes		| A servo is required to fully test this example		|
| Servo - Sweep						| Yes		| A servo is required to fully test this example		|
| SoftwareSerial - SoftwareSerialExample | Yes  | There is no ouput to the serial monitor				|
| SoftwareSerial - TwoPortReceive	| Yes		| None													|
| SPI - BarometricPressureSensor	| Yes		| None													|
| SPI - DigitalPotControl			| Yes		| None													|
| TinyNeoPixel - buttoncycler		| Yes		| None													|
| TinyNeoPixel - RGBWstrandtest		| Yes		| None													|
| TinyNeoPixel - simple				| Yes		| None													|
| TinyNeoPixel - buttoncycler		| Yes		| None													|
| TinyNeoPixel - strandtest			| Yes		| None													|	
| TinyNeoPixel Static - buttoncycler| Yes		| None													|	
| TinyNeoPixel Static - simple		| Yes		| None													|
| Wire - slave_receiver				| Yes		| None													|
| Wire - slave_sender				| Yes		| None													|
		
	