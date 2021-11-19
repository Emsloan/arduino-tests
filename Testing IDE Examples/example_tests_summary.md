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
| EEPROM - eeprom_put				| Yes		| "Serial1" only prints in the "void loop()" function	|
| EEPROM - eeprom_read				| Yes		| Must change "Serial" to "Serial1"						|

	