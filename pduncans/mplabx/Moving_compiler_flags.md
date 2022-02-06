# Moving compiler flags

The process of moving the compiler's flags requires removing flags set in boards.txt and placing them in 
platform.txt.  The flags are originally set by choosing them in the Arduino IDE's menu system.
Boards.txt is the basis of the IDE's menu system and removing menu options means the setting must be toggled 
in another location.  Declarations made in boards.txt will be pulled into the compiler patterns properly 
using the Arduino IDE, but when using Microchip's MPLab X the definitions created in boards.txt will not 
be incorporated into the compiler's patterns.  Errors occur when sketches are uploaded because critical 
variables are never set during compilation. 

```
make -f nbproject/Makefile-default.mk SUBPROJECTS= .build-conf
make[1]: Entering directory 'C:/Users/paulm/Documents/pduncans_blink_avr128DA48.X'
make  -f nbproject/Makefile-default.mk dist/default/production/pduncans_blink_avr128DA48.X.production.hex
make[2]: Entering directory 'C:/Users/paulm/Documents/pduncans_blink_avr128DA48.X'
"C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\avr-g++.exe"  -mmcu=avr128da48 -I "C:/Users/paulm/.mchp_packs/Microchip/AVR-Dx_DFP/2.0.151/include" -B "C:/Users/paulm/.mchp_packs/Microchip/AVR-Dx_DFP/2.0.151/gcc/dev/avr128da48"  -x c++ -c -D__AVR128DA48__  -I"imported-core" -funsigned-char -funsigned-bitfields -Os -ffunction-sections -fdata-sections -fpack-struct -fshort-enums -DF_CPU=24000000L -DARDUINO=10802 -Davrda -DIDE=Arduino -I "imported-core/api/deprecated" -Wall -MD -MP -MF "build/default/production/imported-core/UART.o.d" -MT "build/default/production/imported-core/UART.o.d" -MT build/default/production/imported-core/UART.o  -o build/default/production/imported-core/UART.o imported-core/UART.cpp  -DXPRJ_default=default    -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -mrelax -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0 -std=gnu++11
"C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\avr-g++.exe"   -mmcu=avr128da48 -I "C:/Users/paulm/.mchp_packs/Microchip/AVR-Dx_DFP/2.0.151/include" -B "C:/Users/paulm/.mchp_packs/Microchip/AVR-Dx_DFP/2.0.151/gcc/dev/avr128da48"  -x c -c -D__AVR128DA48__  -I"imported-core" -funsigned-char -funsigned-bitfields -Os -ffunction-sections -fdata-sections -fpack-struct -fshort-enums -DF_CPU=24000000L -DARDUINO=10802 -Davrda -DIDE=Arduino  -I "imported-core/api/deprecated" -Wall -MD -MP -MF "build/default/production/imported-core/wiring_analog.o.d" -MT "build/default/production/imported-core/wiring_analog.o.d" -MT build/default/production/imported-core/wiring_analog.o  -o build/default/production/imported-core/wiring_analog.o imported-core/wiring_analog.c  -DXPRJ_default=default    -Wall -std=gnu11 -ffunction-sections -fdata-sections -MMD -fno-fat-lto-objects -mrelax -Werror=implicit-function-declaration -Wundef -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0
"C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\avr-g++.exe"   -mmcu=avr128da48 -I "C:/Users/paulm/.mchp_packs/Microchip/AVR-Dx_DFP/2.0.151/include" -B "C:/Users/paulm/.mchp_packs/Microchip/AVR-Dx_DFP/2.0.151/gcc/dev/avr128da48"  -x c -c -D__AVR128DA48__  -I"imported-core" -funsigned-char -funsigned-bitfields -Os -ffunction-sections -fdata-sections -fpack-struct -fshort-enums -DF_CPU=24000000L -DARDUINO=10802 -Davrda -DIDE=Arduino  -I "imported-core/api/deprecated" -Wall -MD -MP -MF "build/default/production/imported-core/wiring_digital.o.d" -MT "build/default/production/imported-core/wiring_digital.o.d" -MT build/default/production/imported-core/wiring_digital.o  -o build/default/production/imported-core/wiring_digital.o imported-core/wiring_digital.c  -DXPRJ_default=default    -Wall -std=gnu11 -ffunction-sections -fdata-sections -MMD -fno-fat-lto-objects -mrelax -Werror=implicit-function-declaration -Wundef -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0
In file included from imported-core/core_devices.h:11:0,
                 from imported-core/Arduino.h:27,
                 from imported-core/UART.cpp:22:
imported-core/core_parameters.h:17:8: warning: #warning "All of the version defines are missing, please correct your build environment; it is likely failing to define other critical values" [-Wcpp]
       #warning "All of the version defines are missing, please correct your build environment; it is likely failing to define other critical values"
        ^~~~~~~
In file included from imported-core/core_devices.h:11:0,
                 from imported-core/Arduino.h:27,
                 from imported-core/wiring_private.h:30,
                 from imported-core/wiring_digital.c:26:
imported-core/core_parameters.h:17:8: warning: #warning "All of the version defines are missing, please correct your build environment; it is likely failing to define other critical values" [-Wcpp]
       #warning "All of the version defines are missing, please correct your build environment; it is likely failing to define other critical values"
        ^~~~~~~
In file included from imported-core/core_devices.h:11:0,
                 from imported-core/Arduino.h:27,
                 from imported-core/wiring_private.h:30,
                 from imported-core/wiring_analog.c:25:
imported-core/core_parameters.h:17:8: warning: #warning "All of the version defines are missing, please correct your build environment; it is likely failing to define other critical values" [-Wcpp]
       #warning "All of the version defines are missing, please correct your build environment; it is likely failing to define other critical values"
        ^~~~~~~
nbproject/Makefile-default.mk:501: recipe for target 'build/default/production/imported-core/UART.o' failed
imported-core/UART.cpp: In member function 'virtual void UartClass::begin(long unsigned int, uint16_t)':
imported-core/UART.cpp:375:27: error: 'USART_RXMODE0_bm' was not declared in this scope
     ctrlb              |= USART_RXMODE0_bm;         // set the U2X bit in what will become CTRLB
                           ^~~~~~~~~~~~~~~~
imported-core/UART.cpp:375:27: note: suggested alternative: 'USART_RXMODE_0_bm'
     ctrlb              |= USART_RXMODE0_bm;         // set the U2X bit in what will become CTRLB
                           ^~~~~~~~~~~~~~~~
                           USART_RXMODE_0_bm
make[2]: *** [build/default/production/imported-core/UART.o] Error 1
make[2]: *** Waiting for unfinished jobs....
nbproject/Makefile-default.mk:291: recipe for target 'build/default/production/imported-core/wiring_digital.o' failed
In file included from imported-core/wiring_private.h:30:0,
nbproject/Makefile-default.mk:285: recipe for target 'build/default/production/imported-core/wiring_analog.o' failed
In function 'check_constant_pin',
make[2]: Leaving directory 'C:/Users/paulm/Documents/pduncans_blink_avr128DA48.X'
                 from imported-core/wiring_digital.c:26:
    inlined from 'digitalWriteFast' at imported-core/wiring_digital.c:420:3:
nbproject/Makefile-default.mk:95: recipe for target '.build-conf' failed
imported-core/Arduino.h:58:5: error: call to 'badArg' declared with attribute error: 
make[1]: Leaving directory 'C:/Users/paulm/Documents/pduncans_blink_avr128DA48.X'
     badArg("Fast digital pin must be a constant");
nbproject/Makefile-impl.mk:39: recipe for target '.build-impl' failed
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In function 'check_constant_pin',
    inlined from 'digitalReadFast' at imported-core/wiring_digital.c:478:3:
imported-core/Arduino.h:58:5: error: call to 'badArg' declared with attribute error: 
     badArg("Fast digital pin must be a constant");
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In function 'check_constant_pin',
    inlined from 'openDrainFast' at imported-core/wiring_digital.c:511:3:
imported-core/Arduino.h:58:5: error: call to 'badArg' declared with attribute error: 
     badArg("Fast digital pin must be a constant");
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In function 'check_constant_pin',
    inlined from 'pinModeFast' at imported-core/wiring_digital.c:534:3:
imported-core/Arduino.h:58:5: error: call to 'badArg' declared with attribute error: 
     badArg("Fast digital pin must be a constant");
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
imported-core/wiring_digital.c: In function 'pinModeFast':
imported-core/wiring_digital.c:536:5: error: call to 'badArg' declared with attribute error: 
     badArg("mode must be constant when used with pinModeFast");
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make[2]: *** [build/default/production/imported-core/wiring_digital.o] Error 1
imported-core/wiring_analog.c: In function 'resumeTCD0':
imported-core/wiring_analog.c:734:3: error: call to 'badCall' declared with attribute error: 
   badCall("Resuming core control of type D timer not supported.");
   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make[2]: *** [build/default/production/imported-core/wiring_analog.o] Error 1
make[1]: *** [.build-conf] Error 2
make: *** [.build-impl] Error 2

BUILD FAILED (exit value 2, total time: 412ms)

```

It can also be seen above that the compiler patterns are not the same when comparing them to the patterns
created in platform.txt:
```

####################
# Compile Patterns #
####################

## Compile c files
recipe.c.o.pattern="{compiler.path}{compiler.c.cmd}" {compiler.c.flags} -mmcu={build.mcu} {build.optiondefines} {build.versiondefines} {compiler.c.extra_flags} {build.extra_flags} "-I{build.core.path}/api/deprecated" {includes} "{source_file}" -o "{object_file}"

## Compile c++ files
recipe.cpp.o.pattern="{compiler.path}{compiler.cpp.cmd}" {compiler.cpp.flags} -mmcu={build.mcu} {build.optiondefines} {build.versiondefines} {compiler.cpp.extra_flags} {build.extra_flags} "-I{build.core.path}/api/deprecated" {includes} "{source_file}" -o "{object_file}"

## Compile S files
recipe.S.o.pattern="{compiler.path}{compiler.c.cmd}" {compiler.S.flags} -mmcu={build.mcu} {build.optiondefines} {build.versiondefines} {compiler.S.extra_flags} {build.extra_flags} "-I{build.core.path}/api/deprecated" {includes} "{source_file}" -o "{object_file}"

```

These patterns are written out correctly in the Arduino IDE during the compilation process. 
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_352325\\sketch\\sketch_jan17a.ino.cpp" -o nul
Generating function prototypes...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_352325\\sketch\\sketch_jan17a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_352325\\preproc\\ctags_target_for_gcc_minus_e.cpp"
"C:\\Users\\paulm\\Downloads\\arduino-1.8.16-windows\\arduino-1.8.16\\tools-builder\\ctags\\5.8-arduino11/ctags" -u --language-force=c++ -f - --c++-kinds=svpf --fields=KSTtzns --line-directives "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_352325\\preproc\\ctags_target_for_gcc_minus_e.cpp"
Compiling sketch...
```


## How to move compiler flags

In platform.txt the necessary flags should be set in this manner:
```
build.optiondefines=-DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2

# Extra declarations to test moving setting from boards.txt 
build.clocksource=0
build.wireabr=.wO
build.millis=-DMILLIS_USE_TIMERB2
```

The "build.", "bootloader.", "compiler."...etc declare a variable that can be set after the equals sign.  The set variable's definition will be entered
into compiler recipes.  Boards.txt and platform.txt use the "\{\}" operators to indicate where the values should 
be replaced with the set definition.   


