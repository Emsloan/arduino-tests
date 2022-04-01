Error Messages:

Arduino: 1.8.16 (Mac OS X), Board: "AVR128DB48 Curiosity Nano, AVR128DB48"

/Applications/Arduino.app/Contents/Java/arduino-builder -dump-prefs -logger=machine -hardware /Applications/Arduino.app/Contents/Java/hardware -hardware /Users/jembox/Library/Arduino15/packages -tools /Applications/Arduino.app/Contents/Java/tools-builder -tools /Applications/Arduino.app/Contents/Java/hardware/tools/avr -tools /Users/jembox/Library/Arduino15/packages -built-in-libraries /Applications/Arduino.app/Contents/Java/libraries -libraries /Users/jembox/Documents/Arduino/libraries -fqbn=Microchip:megaavr:avrdb:chip=avr128db48 -ide-version=10816 -build-path /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133 -warnings=none -build-cache /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_cache_146860 -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.avr-gcc.path=/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b -prefs=runtime.tools.avr-gcc-7.3.0-atmel3.6.1-azduino4b.path=/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b -prefs=runtime.tools.avrdude.path=/Users/jembox/Library/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino18 -prefs=runtime.tools.avrdude-6.3.0-arduino18.path=/Users/jembox/Library/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino18 -verbose /Users/jembox/OneDrive/ASU/SER_402/arduino-tests/jthoma74_Mac_Tests/Apple_Intel/WireExampleTests/master_reader/master_reader.ino
/Applications/Arduino.app/Contents/Java/arduino-builder -compile -logger=machine -hardware /Applications/Arduino.app/Contents/Java/hardware -hardware /Users/jembox/Library/Arduino15/packages -tools /Applications/Arduino.app/Contents/Java/tools-builder -tools /Applications/Arduino.app/Contents/Java/hardware/tools/avr -tools /Users/jembox/Library/Arduino15/packages -built-in-libraries /Applications/Arduino.app/Contents/Java/libraries -libraries /Users/jembox/Documents/Arduino/libraries -fqbn=Microchip:megaavr:avrdb:chip=avr128db48 -ide-version=10816 -build-path /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133 -warnings=none -build-cache /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_cache_146860 -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.avr-gcc.path=/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b -prefs=runtime.tools.avr-gcc-7.3.0-atmel3.6.1-azduino4b.path=/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b -prefs=runtime.tools.avrdude.path=/Users/jembox/Library/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino18 -prefs=runtime.tools.avrdude-6.3.0-arduino18.path=/Users/jembox/Library/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino18 -verbose /Users/jembox/OneDrive/ASU/SER_402/arduino-tests/jthoma74_Mac_Tests/Apple_Intel/WireExampleTests/master_reader/master_reader.ino
Using board 'avrdb' from platform in folder: /Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1
Using core 'dxcore' from platform in folder: /Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1
Detecting libraries used...
/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b/bin/avr-g++ -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/cores/dxcore/api/deprecated -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/cores/dxcore -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/variants/48pin-standard /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/sketch/master_reader.ino.cpp -o /dev/null
Alternatives for Wire.h: [Wire@2.0.5]
ResolveLibrary(Wire.h)
  -> candidates: [Wire@2.0.5]
/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b/bin/avr-g++ -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/cores/dxcore/api/deprecated -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/cores/dxcore -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/variants/48pin-standard -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/sketch/master_reader.ino.cpp -o /dev/null
Using cached library dependencies for file: /Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/Wire.cpp
Using cached library dependencies for file: /Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c
Using cached library dependencies for file: /Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi_pins.c
Using cached library dependencies for file: /Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/utility/twi.c
Generating function prototypes...
/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b/bin/avr-g++ -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/cores/dxcore/api/deprecated -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/cores/dxcore -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/variants/48pin-standard -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/sketch/master_reader.ino.cpp -o /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/preproc/ctags_target_for_gcc_minus_e.cpp
/Applications/Arduino.app/Contents/Java/tools-builder/ctags/5.8-arduino11/ctags -u --language-force=c++ -f - --c++-kinds=svpf --fields=KSTtzns --line-directives /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/preproc/ctags_target_for_gcc_minus_e.cpp
Compiling sketch...
/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b/bin/avr-g++ -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/cores/dxcore/api/deprecated -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/cores/dxcore -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/variants/48pin-standard -I/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/sketch/master_reader.ino.cpp -o /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/sketch/master_reader.ino.cpp.o
Compiling libraries...
Compiling library "Wire"
Using previously compiled file: /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o
Using previously compiled file: /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi_pins.c.o
Using previously compiled file: /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/Wire.cpp.o
Using previously compiled file: /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o
Compiling core...
Using precompiled core: /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_cache_146860/core/core_Microchip_megaavr_avrdb_chip_avr128db48_2b8854230e041952c0c374b3636a1176.a
Linking everything together...
/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128db48 -o /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/master_reader.ino.elf /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/sketch/master_reader.ino.cpp.o /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi_pins.c.o /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/Wire.cpp.o /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o /var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/../arduino_cache_146860/core/core_Microchip_megaavr_avrdb_chip_avr128db48_2b8854230e041952c0c374b3636a1176.a -L/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133 -lm
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o (symbol from plugin): In function `TWI_SlaveInit':
(.text+0x0): multiple definition of `TWI_SlaveInit'
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o (symbol from plugin):(.text+0x0): first defined here
/Users/jembox/Library/Arduino15/packages/Microchip/tools/avr-gcc/7.3.0-atmel3.6.1-azduino4b/bin/../lib/gcc/avr/7.3.0/../../../../avr/bin/ld: Disabling relaxation: it will not work with multiple definitions
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o (symbol from plugin): In function `TWI_SlaveInit':
(.text+0x0): multiple definition of `TWI_Flush'
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o (symbol from plugin):(.text+0x0): first defined here
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o (symbol from plugin): In function `TWI_SlaveInit':
(.text+0x0): multiple definition of `TWI_Disable'
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o (symbol from plugin):(.text+0x0): first defined here
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o (symbol from plugin): In function `TWI_SlaveInit':
(.text+0x0): multiple definition of `TWI_MasterSetBaud'
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o (symbol from plugin):(.text+0x0): first defined here
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o (symbol from plugin): In function `TWI_SlaveInit':
(.text+0x0): multiple definition of `TWI_MasterInit'
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o (symbol from plugin):(.text+0x0): first defined here
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o (symbol from plugin): In function `TWI_SlaveInit':
(.text+0x0): multiple definition of `TWI_MasterWrite'
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o (symbol from plugin):(.text+0x0): first defined here
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o (symbol from plugin): In function `TWI_SlaveInit':
(.text+0x0): multiple definition of `TWI_MasterRead'
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/twi.c.o (symbol from plugin):(.text+0x0): first defined here
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/utility/twi.c.o (symbol from plugin): In function `TWI_SlaveInit':
(.text+0x0): multiple definition of `__vector_18'
/var/folders/tv/27v48g250vd1crrbhq2mdhc00000gn/T/arduino_build_206133/libraries/Wire/Wire.cpp.o (symbol from plugin):(.text+0x0): first defined here
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/utility/twi.c:63:6: warning: type of 'TWI_MasterInit' does not match original declaration [-Wlto-type-mismatch]
 void TWI_MasterInit(uint32_t frequency) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:52:6: note: type mismatch in parameter 1
 void TWI_MasterInit(struct twiData *_data) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:52:6: note: 'TWI_MasterInit' was previously declared here
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:52:6: note: code may be misoptimized unless -fno-strict-aliasing is used
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/utility/twi.c:220:6: warning: type of 'TWI_MasterSetBaud' does not match original declaration [-Wlto-type-mismatch]
 void TWI_MasterSetBaud(uint32_t frequency) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:234:6: note: type mismatch in parameter 1
 void TWI_MasterSetBaud(struct twiData *_data, uint32_t frequency) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:234:6: note: 'TWI_MasterSetBaud' was previously declared here
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:234:6: note: code may be misoptimized unless -fno-strict-aliasing is used
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/utility/twi.c:317:9: warning: type of 'TWI_MasterRead' does not match original declaration [-Wlto-type-mismatch]
 uint8_t TWI_MasterRead(uint8_t slave_address,
         ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:373:9: note: type mismatch in parameter 1
 uint8_t TWI_MasterRead(struct twiData *_data, uint8_t bytesToRead, bool send_stop) {
         ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:373:9: note: 'TWI_MasterRead' was previously declared here
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/utility/twi.c:294:9: warning: type of 'TWI_MasterWrite' does not match original declaration [-Wlto-type-mismatch]
 uint8_t TWI_MasterWrite(uint8_t slave_address,
         ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:275:9: note: type mismatch in parameter 1
 uint8_t TWI_MasterWrite(struct twiData *_data, bool send_stop)  {
         ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:275:9: note: 'TWI_MasterWrite' was previously declared here
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:275:9: note: code may be misoptimized unless -fno-strict-aliasing is used
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/utility/twi.c:170:6: warning: type of 'TWI_Disable' does not match original declaration [-Wlto-type-mismatch]
 void TWI_Disable(void) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:167:6: note: type mismatch in parameter 1
 void TWI_Disable(struct twiData *_data) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:167:6: note: 'TWI_Disable' was previously declared here
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/utility/twi.c:159:6: warning: type of 'TWI_Flush' does not match original declaration [-Wlto-type-mismatch]
 void TWI_Flush(void) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:141:6: note: type mismatch in parameter 1
 void TWI_Flush(struct twiData *_data) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:141:6: note: 'TWI_Flush' was previously declared here
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/utility/twi.c:113:6: warning: type of 'TWI_SlaveInit' does not match original declaration [-Wlto-type-mismatch]
 void TWI_SlaveInit(uint8_t address, uint8_t receive_broadcast, uint8_t second_address) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:100:6: note: type mismatch in parameter 1
 void TWI_SlaveInit(struct twiData *_data, uint8_t address, uint8_t receive_broadcast, uint8_t second_address) {
      ^
/Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire/src/twi.c:100:6: note: 'TWI_SlaveInit' was previously declared here
collect2: error: ld returned 1 exit status
Using library Wire at version 2.0.5 in folder: /Users/jembox/Library/Arduino15/packages/Microchip/hardware/megaavr/1.0.1/libraries/Wire 
exit status 1
Error compiling for board AVR128DB48 Curiosity Nano.
