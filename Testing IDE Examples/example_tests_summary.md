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
| Opamp - Inverting_amplifier		| No		| 'Opamp0' object is not defined when running			|
| Opamp - Inverting_amplifier_with_follower| No | 'Opampx' objects are undefined						|
| Opamp - Non_inverting_amplifier	| No		| init() function doesn't setup variables properly		|
| Opamp - Voltage_follower			| No 		| init() function doesn't setup variables properly		|
| Servo_DxCore - Knob				| Yes		| None													|
| Servo_DxCore - ServoMaxTest		| Yes		| None													|
| Servo_DxCore - Sweep				| Yes		| None													|
| Logic - Three_input_AND			| Yes		| AND remains off regardless of input status			|
| Logic - Three_input_NAND			| Yes		| NAND remains on regardless of input status			|
| Logic - Three_input_OR			| Yes		| OR gate remains on regardless of input status			|   
	