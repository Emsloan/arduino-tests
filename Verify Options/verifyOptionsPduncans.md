# Verification of Option Settings

### Testing DA48 1 wire, printf no float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2
```

### Testing DA48 2 wire, printf no float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2
```

### Testing DA48 1 wire, printf min float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2
```

### Printf
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc" -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128da48 -Wl,-u,vfprintf -lprintf_min -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/sketch_apr02a.ino.elf" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/core\\core.a" "-LC:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527" -lm
```

```
-Wl,-u,vfprintf -lprintf_min
```

### Testing DA48 2 wire, printf min float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2
```

### Printf
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc" -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128da48 -Wl,-u,vfprintf -lprintf_min -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/sketch_apr02a.ino.elf" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/core\\core.a" "-LC:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527" -lm
```

```
-Wl,-u,vfprintf -lprintf_min
```

### Testing DA48 1 wire, printf full float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2
```

### Printf
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc" -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128da48 -Wl,-u,vfprintf -lprintf_flt -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/sketch_apr02a.ino.elf" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/core\\core.a" "-LC:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527" -lm
```

```
-Wl,-u,vfprintf -lprintf_flt
```

### Testing DA48 2 wire, printf full float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128da48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrda -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 -DMILLIS_USE_TIMERB2 -DCLOCK_SOURCE=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2
```

### Printf
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc" -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128da48 -Wl,-u,vfprintf -lprintf_flt -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/sketch_apr02a.ino.elf" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/core\\core.a" "-LC:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527" -lm
```

```
-Wl,-u,vfprintf -lprintf_flt
```

### Testing DB48 1 wire, printf no float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2
```

### Testing DB48 2 wire, printf no float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2
```

### Testing DB48 1 wire, printf min float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2
```

### Printf
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc" -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128db48 -Wl,-u,vfprintf -lprintf_min -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/sketch_apr02a.ino.elf" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/core\\core.a" "-LC:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527" -lm
```

```
-Wl,-u,vfprintf -lprintf_min
```

### Testing DB48 2 wire, printf min float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2
```

### Printf
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc" -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128db48 -Wl,-u,vfprintf -lprintf_min -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/sketch_apr02a.ino.elf" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/core\\core.a" "-LC:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527" -lm
```

```
-Wl,-u,vfprintf -lprintf_min
```

### Testing DB48 1 wire, printf full float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_SINGLE -DMILLIS_USE_TIMERB2
```

### Printf
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc" -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128db48 -Wl,-u,vfprintf -lprintf_flt -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/sketch_apr02a.ino.elf" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/core\\core.a" "-LC:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527" -lm
```

```
-Wl,-u,vfprintf -lprintf_flt
```

### Testing DB48 2 wire, printf full float
### Wire
```
Compiling sketch...
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-g++" -c -g -Os -Wall -std=gnu++17 -fpermissive -Wno-sized-deallocation -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -Wno-error=narrowing -MMD -flto -mrelax -mmcu=avr128db48 -DF_CPU=24000000L -DCLOCK_SOURCE=0 -DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2 -DARDUINO=10819 -DARDUINO_avrdb -DARDUINO_ARCH_MEGAAVR "-DDXCORE=\"1.0.1\"" -DDXCORE_MAJOR=1UL -DDXCORE_MINOR=0UL -DDXCORE_PATCH=1UL -DDXCORE_RELEASED=0 "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore/api/deprecated" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\cores\\dxcore" "-IC:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\hardware\\megaavr\\1.0.1\\variants\\48pin-standard" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp" -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o"
Compiling libraries...
```

```
-DCORE_ATTACH_ALL -DTWI_MORS_BOTH -DMILLIS_USE_TIMERB2
```

### Printf
```
"C:\\Users\\paulm\\AppData\\Local\\Arduino15\\packages\\Microchip\\tools\\avr-gcc\\7.3.0-atmel3.6.1-azduino4b/bin/avr-gcc" -Wall -Os -g -flto -fuse-linker-plugin -mrelax -Wl,--gc-sections,--section-start=.text=0x0,--section-start=.FLMAP_SECTION1=0x8000,--section-start=.FLMAP_SECTION2=0x10000,--section-start=.FLMAP_SECTION3=0x18000 -mmcu=avr128db48 -Wl,-u,vfprintf -lprintf_flt -o "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/sketch_apr02a.ino.elf" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527\\sketch\\sketch_apr02a.ino.cpp.o" "C:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527/core\\core.a" "-LC:\\Users\\paulm\\AppData\\Local\\Temp\\arduino_build_373527" -lm
```

```
-Wl,-u,vfprintf -lprintf_flt
```
