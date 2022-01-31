# Changing compiler flags 

Compiler flags are set during the compilation of an Arduino sketch and are used to compile the code in 
an optimized manner.  Developers use flags to create an executatble package that is compiled in the manner in which
they desire.

### Current compiler flags during sketch uploading in IDE
```
Detecting libraries used...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os 
-Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics 
-Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL 
-DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" 
-DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 
"-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\sketch\\sketch_jan19a.ino.cpp" -o nul
Generating function prototypes...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\sketch\\sketch_jan19a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\preproc\\ctags_target_for_gcc_minus_e.cpp"
"C:\\Users\\paulm\\Downloads\\arduino-1.8.16-windows\\arduino-1.8.16\\tools-builder\\ctags\\5.8-arduino11/ctags" -u --language-force=c++ -f - --c++-kinds=svpf --fields=KSTtzns --line-directives "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\preproc\\ctags_target_for_gcc_minus_e.cpp"
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\sketch\\sketch_jan19a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\sketch\\sketch_jan19a.ino.cpp.o"
Compiling libraries...
```

### Flags set in platforms.txt
```
##############################
# DxCore-related definitions #
##############################
name=DxCore
versionnum.major=1
versionnum.minor=4
versionnum.patch=6
versionnum.postfix=
versionnum.released=0
version={versionnum.major}.{versionnum.minor}.{versionnum.patch}{versionnum.postfix}
build.versiondefines=-DARDUINO={runtime.ide.version} -DARDUINO_{build.board} -DARDUINO_ARCH_{build.arch} -DDXCORE="{version}" -DDXCORE_MAJOR={versionnum.major}UL -DDXCORE_MINOR={versionnum.minor}UL -DDXCORE_PATCH={versionnum.patch}UL -DDXCORE_RELEASED={versionnum.released}

build.optiondefines=-DF_CPU={build.f_cpu} -DCLOCK_SOURCE={build.clocksource} {build.attachmode} -DTWI_{build.wire.mode} -DMILLIS_USE_TIMER{build.millistimer}
```

```

#####################
# Compile Parameter #
#####################

# Force users to see warnings, since it defaults to them being off if you let the IDE have it's way.
compiler.warning_flags=-Wall
compiler.warning_flags.none=-Wall
compiler.warning_flags.default=-Wall
compiler.warning_flags.more=-Wall
compiler.warning_flags.all=-Wall -Wextra

# Default "compiler.path" is correct, change only if you want to override the initial value
compiler.path={runtime.tools.avr-gcc.path}/bin/
compiler.c.cmd=avr-gcc
compiler.c.flags=-c -g -Os {compiler.warning_flags} -std=gnu11 -ffunction-sections -fdata-sections -MMD -flto -fno-fat-lto-objects -mrelax -Werror=implicit-function-declaration -Wundef
# DxCore has the three additional FLMAP sections for mapped flash
compiler.c.elf.flags={compiler.warning_flags} -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start={build.text_section_start},--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000
compiler.c.elf.cmd=avr-gcc
compiler.S.flags=-c -g -x assembler-with-cpp -flto -MMD
compiler.cpp.cmd=avr-g++
compiler.cpp.flags=-c -g -Os {compiler.warning_flags} -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax
compiler.ar.cmd=avr-gcc-ar
compiler.ar.flags=rcs
compiler.objcopy.cmd=avr-objcopy
compiler.objcopy.eep.flags=-O ihex -j .eeprom --set-section-flags=.eeprom=alloc,load --no-change-warnings --change-section-lma .eeprom=0
compiler.objdump.cmd=avr-objdump
compiler.objdump.flags=--disassemble --source --line-numbers --demangle --section=.text
compiler.nm.cmd=avr-nm
compiler.nm.flags=--numeric-sort --line-numbers --demangle --print-size --format=s
compiler.elf2hex.flags=-O ihex -R .eeprom
compiler.elf2hex.bin.flags=-O binary -R .eeprom
compiler.elf2hex.cmd=avr-objcopy
compiler.ldflags=
compiler.libraries.ldflags=
compiler.size.cmd=avr-size
```

### Adding or removing standard cpp flags 
Changing the c++ flags found in platforms.txt appears to be done by changing this line of code:
```
compiler.cpp.flags=-c -g -Os {compiler.warning_flags} -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax
```

These flags get added to these lines in the IDE's compilation:
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\sketch\\sketch_jan19a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\preproc\\ctags_target_for_gcc_minus_e.cpp"

and

"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\sketch\\sketch_jan19a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_884040\\sketch\\sketch_jan19a.ino.cpp.o"
```

### Adding or removing build options
Changing the build options require setting variables in boards.txt and through the IDE's menu system.  These settings are then used in 
platforms.txt to set flags for build options in the IDE. 
Changing the flags occurs in platforms.txt here:
```
build.versiondefines=-DARDUINO={runtime.ide.version} -DARDUINO_{build.board} -DARDUINO_ARCH_{build.arch} -DDXCORE="{version}" -DDXCORE_MAJOR={versionnum.major}UL -DDXCORE_MINOR={versionnum.minor}UL -DDXCORE_PATCH={versionnum.patch}UL -DDXCORE_RELEASED={versionnum.released}

build.optiondefines=-DF_CPU={build.f_cpu} -DCLOCK_SOURCE={build.clocksource} {build.attachmode} -DTWI_{build.wire.mode} -DMILLIS_USE_TIMER{build.millistimer}
```
These flags can be viewed in the IDE's verbose output here:
```
Detecting libraries used...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os 
-Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics 
-Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL 
-DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" 
-DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 
```

# Changing Flags

### Removing -g -Os
IDE output after changing platforms.txt:
```
Detecting libraries used...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_814046\\sketch\\sketch_jan19a.ino.cpp" -o nul
Generating function prototypes...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -flto -mrelax -w -x c++ -E -CC -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_814046\\sketch\\sketch_jan19a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_814046\\preproc\\ctags_target_for_gcc_minus_e.cpp"

```
Changing platforms.txt by removing the -g and -Os flags has removed them from the compilation.

### Adding -O0 flag to platforms.txt
IDE output after changing platforms.txt:
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -O0 -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10816 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.4.6\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=4UL -DDXCORE_PATCH=6UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\DxCore\\hardware\\megaavr\\1.4.6\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_617891\\sketch\\sketch_jan19a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_617891\\sketch\\sketch_jan19a.ino.cpp.o"
Compiling libraries...

```
The -O0 flag is now used during compilation.


