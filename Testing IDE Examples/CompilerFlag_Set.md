
You can also do it from the command line: --build-properties

This will override the value of the build.extra_flags property that could have been set in  boards.txt.

```sh
arduino-cli compile --fqbn Microchip:megaavr:avrda --build-properties build.extra_flags=-DFLAGNAME SketchName
```

Set up Arduino Boards for arduino-cli using: arduino-cli core install arduino:avr

Get FQBN of installed board using 'arduino-cli board listall' 

```sh
Jemimahs-MacBook-Pro:jthoma74_blink_NanoEvery jembox$ arduino-cli board listall
Board Name            FQBN
AVR DA-series         Microchip:megaavr:avrda
Arduino Nano Every    arduino:megaavr:nona4809
Arduino Uno WiFi Rev2 arduino:megaavr:uno2018
```sh

Use FQBN in arduino-cli 

```sh
arduino-cli compile --fqbn Microchip:megaavr:avrda --build-properties build.extra_flags=-DFLAGNAME jthoma74_FlagTest
```

Result:

```sh
Jemimahs-MacBook-Pro:jthoma74_FlagTest jembox$ arduino-cli compile --fqbn Microchip:megaavr:avrda --build-property build.extra_flags=-TESTFLAG jthoma74_FlagTest.ino
Sketch uses 1002 bytes (0%) of program storage space. Maximum is 131072 bytes.
Global variables use 4 bytes (0%) of dynamic memory, leaving 16380 bytes for local variables. Maximum is 16384 bytes.
```sh