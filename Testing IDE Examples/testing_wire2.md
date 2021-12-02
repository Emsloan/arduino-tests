# Wire - pinswap_via_swap, pinswap_via_pins, SFRRanger_reader

### Example Code
```
// Wire pinswapping via Wire.pins()
// Copy of Wire Master Reader
// except for the Wire.pins() call.
// This is mostly here to make sure it gets tested by CI.


#include <Wire.h>

void setup() {
  Wire.swap(2);        // Choose pin swapping level 2 (PC2/PC3 master/slave)
  Wire.begin();        // join i2c bus (address optional for master)
  Serial.begin(9600);  // start serial for output
}

void loop() {
  Wire.requestFrom(8, 6);    // request 6 bytes from slave device #8

  while (Wire.available()) { // slave may send less than requested
    char c = Wire.read(); // receive a byte as character
    Serial.print(c);         // print the character
  }

  delay(500);
}
```
```
// Wire pinswapping via Wire.pins()
// Copy of Wire Master Reader
// except for the Wire.pins() call.
// This is mostly here to make sure it gets tested by CI.


#include <Wire.h>

void setup() {
  Wire.pins(PIN_PC2, PIN_PC3); // Choose the PC2/PC3 pinset for the TWI interface
  Wire.begin();        // join i2c bus (address optional for master)
  Serial.begin(9600);  // start serial for output
}

void loop() {
  Wire.requestFrom(8, 6);    // request 6 bytes from slave device #8

  while (Wire.available()) { // slave may send less than requested
    char c = Wire.read(); // receive a byte as character
    Serial.print(c);         // print the character
  }

  delay(500);
}


```
```
// I2C SRF10 or SRF08 Devantech Ultrasonic Ranger Finder
// by Nicholas Zambetti <http://www.zambetti.com>
// and James Tichenor <http://www.jamestichenor.net>

// Demonstrates use of the Wire library reading data from the
// Devantech Utrasonic Rangers SFR08 and SFR10

// Created 29 April 2006

// This example code is in the public domain.


#include <Wire.h>

void setup() {
  Wire.begin();                // join i2c bus (address optional for master)
  Serial.begin(9600);          // start serial communication at 9600bps
}

int reading = 0;

void loop() {
  // step 1: instruct sensor to read echoes
  Wire.beginTransmission(112); // transmit to device #112 (0x70)
  // the address specified in the datasheet is 224 (0xE0)
  // but i2c addressing uses the high 7 bits so it's 112
  Wire.write(byte(0x00));      // sets register pointer to the command register (0x00)
  Wire.write(byte(0x50));      // command sensor to measure in "inches" (0x50)
  // use 0x51 for centimeters
  // use 0x52 for ping microseconds
  Wire.endTransmission();      // stop transmitting

  // step 2: wait for readings to happen
  delay(70);                   // datasheet suggests at least 65 milliseconds

  // step 3: instruct sensor to return a particular echo reading
  Wire.beginTransmission(112); // transmit to device #112
  Wire.write(byte(0x02));      // sets register pointer to echo #1 register (0x02)
  Wire.endTransmission();      // stop transmitting

  // step 4: request reading from sensor
  Wire.requestFrom(112, 2);    // request 2 bytes from slave device #112

  // step 5: receive reading from sensor
  if (2 <= Wire.available()) { // if two bytes were received
    reading = Wire.read();  // receive high byte (overwrites previous reading)
    reading = reading << 8;    // shift high byte to be high 8 bits
    reading |= Wire.read(); // receive low byte as lower 8 bits
    Serial.println(reading);   // print the reading
  }

  delay(250);                  // wait a bit since people have to read the output :)
}


/*

// The following code changes the address of a Devantech Ultrasonic Range Finder (SRF10 or SRF08)
// usage: changeAddress(0x70, 0xE6);

void changeAddress(byte oldAddress, byte newAddress) {
  Wire.beginTransmission(oldAddress);
  Wire.write(byte(0x00));
  Wire.write(byte(0xA0));
  Wire.endTransmission();

  Wire.beginTransmission(oldAddress);
  Wire.write(byte(0x00));
  Wire.write(byte(0xAA));
  Wire.endTransmission();

  Wire.beginTransmission(oldAddress);
  Wire.write(byte(0x00));
  Wire.write(byte(0xA5));
  Wire.endTransmission();

  Wire.beginTransmission(oldAddress);
  Wire.write(byte(0x00));
  Wire.write(newAddress);
  Wire.endTransmission();
}

*/
```

### Result
Examples compiled and uploaded successfully to the board.

### Messages
```

Sketch uses 3734 bytes (2%) of program storage space. Maximum is 131072 bytes.
Global variables use 494 bytes (3%) of dynamic memory, leaving 15890 bytes for local variables. Maximum is 16384 bytes.

avrdude: Version 6.3-20201216
         Copyright (c) 2000-2005 Brian Dean, http://www.bdmicro.com/
         Copyright (c) 2007-2014 Joerg Wunsch

         System wide configuration file is "C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0/avrdude.conf"

         Using Port                    : usb
         Using Programmer              : curiosity_updi
avrdude: Found CMSIS-DAP compliant device, using EDBG protocol
         AVR Part                      : AVR128DA48
         Chip Erase delay              : 0 us
         PAGEL                         : P00
         BS2                           : P00
         RESET disposition             : dedicated
         RETRY pulse                   : SCK
         serial program mode           : yes
         parallel program mode         : yes
         Timeout                       : 0
         StabDelay                     : 0
         CmdexeDelay                   : 0
         SyncLoops                     : 0
         ByteDelay                     : 0
         PollIndex                     : 0
         PollValue                     : 0x00
         Memory Detail                 :

                                  Block Poll               Page                       Polled
           Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
           ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
           signature      0     0     0    0 no          3    0      0     0     0 0x00 0x00
           prodsig        0     0     0    0 no        125  125      0     0     0 0x00 0x00
           fuses          0     0     0    0 no          9   16      0     0     0 0x00 0x00
           fuse0          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse1          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse2          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse4          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse5          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse6          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse7          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse8          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           lock           0     0     0    0 no          4    1      0     0     0 0x00 0x00
           data           0     0     0    0 no          0    0      0     0     0 0x00 0x00
           flash          0     0     0    0 no     131072  512      0     0     0 0x00 0x00
           eeprom         0     0     0    0 no        512   32      0     0     0 0x00 0x00

         Programmer Type : JTAGICE3_UPDI
         Description     : Microchip Curiosity in UPDI mode
         ICE hardware version: 0
         ICE firmware version: 1.17 (rel. 514)
         Serial number   : MCHP3280031800001901
         Vtarget         : 3.31 V
         JTAG clock megaAVR/program: 0 kHz
         JTAG clock megaAVR/debug:   0 kHz
         JTAG clock Xmega: 0 kHz
         PDI clock Xmega : 100 kHz

avrdude: Partial Family_ID returned: "    "
avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.01s

avrdude: Device signature = 0x1e9708 (probably avr128da48)
avrdude: NOTE: "flash" memory has been specified, an erase cycle will be performed
         To disable this feature, specify the -D option.
avrdude: erasing chip
avrdude: reading input file "0b11001001"
avrdude: writing fuse5 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse5 written
avrdude: verifying fuse5 memory against 0b11001001:
avrdude: load data fuse5 data from input file 0b11001001:
avrdude: input file 0b11001001 contains 1 bytes
avrdude: reading on-chip fuse5 data:

Reading | ################################################## | 100% 0.00s

avrdude: verifying ...
avrdude: 1 bytes of fuse5 verified
avrdude: reading input file "0x00"
avrdude: writing fuse7 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse7 written
avrdude: verifying fuse7 memory against 0x00:
avrdude: load data fuse7 data from input file 0x00:
avrdude: input file 0x00 contains 1 bytes
avrdude: reading on-chip fuse7 data:

Reading | ################################################## | 100% 0.00s

avrdude: verifying ...
avrdude: 1 bytes of fuse7 verified
avrdude: reading input file "0x00"
avrdude: writing fuse8 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse8 written
avrdude: verifying fuse8 memory against 0x00:
avrdude: load data fuse8 data from input file 0x00:
avrdude: input file 0x00 contains 1 bytes
avrdude: reading on-chip fuse8 data:

Reading | ################################################## | 100% 0.00s

avrdude: verifying ...
avrdude: 1 bytes of fuse8 verified
avrdude: reading input file "C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_627681/pinswap_via_pins.ino.hex"
avrdude: writing flash (3734 bytes):

Writing | ################################################## | 100% 1.26s

avrdude: 3734 bytes of flash written
avrdude: verifying flash memory against C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_627681/pinswap_via_pins.ino.hex:
avrdude: load data flash data from input file C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_627681/pinswap_via_pins.ino.hex:
avrdude: input file C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_627681/pinswap_via_pins.ino.hex contains 3734 bytes
avrdude: reading on-chip flash data:

Reading | ################################################## | 100% 0.69s

avrdude: verifying ...
avrdude: 3734 bytes of flash verified

avrdude done.  Thank you.



```
```
Sketch uses 3734 bytes (2%) of program storage space. Maximum is 131072 bytes.
Global variables use 494 bytes (3%) of dynamic memory, leaving 15890 bytes for local variables. Maximum is 16384 bytes.

avrdude: Version 6.3-20201216
         Copyright (c) 2000-2005 Brian Dean, http://www.bdmicro.com/
         Copyright (c) 2007-2014 Joerg Wunsch

         System wide configuration file is "C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0/avrdude.conf"

         Using Port                    : usb
         Using Programmer              : curiosity_updi
avrdude: Found CMSIS-DAP compliant device, using EDBG protocol
         AVR Part                      : AVR128DA48
         Chip Erase delay              : 0 us
         PAGEL                         : P00
         BS2                           : P00
         RESET disposition             : dedicated
         RETRY pulse                   : SCK
         serial program mode           : yes
         parallel program mode         : yes
         Timeout                       : 0
         StabDelay                     : 0
         CmdexeDelay                   : 0
         SyncLoops                     : 0
         ByteDelay                     : 0
         PollIndex                     : 0
         PollValue                     : 0x00
         Memory Detail                 :

                                  Block Poll               Page                       Polled
           Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
           ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
           signature      0     0     0    0 no          3    0      0     0     0 0x00 0x00
           prodsig        0     0     0    0 no        125  125      0     0     0 0x00 0x00
           fuses          0     0     0    0 no          9   16      0     0     0 0x00 0x00
           fuse0          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse1          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse2          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse4          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse5          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse6          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse7          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse8          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           lock           0     0     0    0 no          4    1      0     0     0 0x00 0x00
           data           0     0     0    0 no          0    0      0     0     0 0x00 0x00
           flash          0     0     0    0 no     131072  512      0     0     0 0x00 0x00
           eeprom         0     0     0    0 no        512   32      0     0     0 0x00 0x00

         Programmer Type : JTAGICE3_UPDI
         Description     : Microchip Curiosity in UPDI mode
         ICE hardware version: 0
         ICE firmware version: 1.17 (rel. 514)
         Serial number   : MCHP3280031800001901
         Vtarget         : 3.31 V
         JTAG clock megaAVR/program: 0 kHz
         JTAG clock megaAVR/debug:   0 kHz
         JTAG clock Xmega: 0 kHz
         PDI clock Xmega : 100 kHz

avrdude: Partial Family_ID returned: "    "
avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.01s

avrdude: Device signature = 0x1e9708 (probably avr128da48)
avrdude: NOTE: "flash" memory has been specified, an erase cycle will be performed
         To disable this feature, specify the -D option.
avrdude: erasing chip
avrdude: reading input file "0b11001001"
avrdude: writing fuse5 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse5 written
avrdude: verifying fuse5 memory against 0b11001001:
avrdude: load data fuse5 data from input file 0b11001001:
avrdude: input file 0b11001001 contains 1 bytes
avrdude: reading on-chip fuse5 data:

Reading | ################################################## | 100% 0.00s

avrdude: verifying ...
avrdude: 1 bytes of fuse5 verified
avrdude: reading input file "0x00"
avrdude: writing fuse7 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse7 written
avrdude: verifying fuse7 memory against 0x00:
avrdude: load data fuse7 data from input file 0x00:
avrdude: input file 0x00 contains 1 bytes
avrdude: reading on-chip fuse7 data:

Reading | ################################################## | 100% 0.00s

avrdude: verifying ...
avrdude: 1 bytes of fuse7 verified
avrdude: reading input file "0x00"
avrdude: writing fuse8 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse8 written
avrdude: verifying fuse8 memory against 0x00:
avrdude: load data fuse8 data from input file 0x00:
avrdude: input file 0x00 contains 1 bytes
avrdude: reading on-chip fuse8 data:

Reading | ################################################## | 100% 0.00s

avrdude: verifying ...
avrdude: 1 bytes of fuse8 verified
avrdude: reading input file "C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_733041/pinswap_via_swap.ino.hex"
avrdude: writing flash (3734 bytes):

Writing | ################################################## | 100% 1.26s

avrdude: 3734 bytes of flash written
avrdude: verifying flash memory against C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_733041/pinswap_via_swap.ino.hex:
avrdude: load data flash data from input file C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_733041/pinswap_via_swap.ino.hex:
avrdude: input file C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_733041/pinswap_via_swap.ino.hex contains 3734 bytes
avrdude: reading on-chip flash data:

Reading | ################################################## | 100% 0.69s

avrdude: verifying ...
avrdude: 3734 bytes of flash verified

avrdude done.  Thank you.




```
```
Sketch uses 4150 bytes (3%) of program storage space. Maximum is 131072 bytes.
Global variables use 629 bytes (3%) of dynamic memory, leaving 15755 bytes for local variables. Maximum is 16384 bytes.

avrdude: Version 6.3-20201216
         Copyright (c) 2000-2005 Brian Dean, http://www.bdmicro.com/
         Copyright (c) 2007-2014 Joerg Wunsch

         System wide configuration file is "C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0/avrdude.conf"

         Using Port                    : usb
         Using Programmer              : curiosity_updi
avrdude: Found CMSIS-DAP compliant device, using EDBG protocol
         AVR Part                      : AVR128DA48
         Chip Erase delay              : 0 us
         PAGEL                         : P00
         BS2                           : P00
         RESET disposition             : dedicated
         RETRY pulse                   : SCK
         serial program mode           : yes
         parallel program mode         : yes
         Timeout                       : 0
         StabDelay                     : 0
         CmdexeDelay                   : 0
         SyncLoops                     : 0
         ByteDelay                     : 0
         PollIndex                     : 0
         PollValue                     : 0x00
         Memory Detail                 :

                                  Block Poll               Page                       Polled
           Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
           ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
           signature      0     0     0    0 no          3    0      0     0     0 0x00 0x00
           prodsig        0     0     0    0 no        125  125      0     0     0 0x00 0x00
           fuses          0     0     0    0 no          9   16      0     0     0 0x00 0x00
           fuse0          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse1          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse2          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse4          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse5          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse6          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse7          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           fuse8          0     0     0    0 no          1    0      0     0     0 0x00 0x00
           lock           0     0     0    0 no          4    1      0     0     0 0x00 0x00
           data           0     0     0    0 no          0    0      0     0     0 0x00 0x00
           flash          0     0     0    0 no     131072  512      0     0     0 0x00 0x00
           eeprom         0     0     0    0 no        512   32      0     0     0 0x00 0x00

         Programmer Type : JTAGICE3_UPDI
         Description     : Microchip Curiosity in UPDI mode
         ICE hardware version: 0
         ICE firmware version: 1.17 (rel. 514)
         Serial number   : MCHP3280031800001901
         Vtarget         : 3.31 V
         JTAG clock megaAVR/program: 0 kHz
         JTAG clock megaAVR/debug:   0 kHz
         JTAG clock Xmega: 0 kHz
         PDI clock Xmega : 100 kHz

avrdude: Partial Family_ID returned: "    "
avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.01s

avrdude: Device signature = 0x1e9708 (probably avr128da48)
avrdude: NOTE: "flash" memory has been specified, an erase cycle will be performed
         To disable this feature, specify the -D option.
avrdude: erasing chip
avrdude: reading input file "0b11001001"
avrdude: writing fuse5 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse5 written
avrdude: verifying fuse5 memory against 0b11001001:
avrdude: load data fuse5 data from input file 0b11001001:
avrdude: input file 0b11001001 contains 1 bytes
avrdude: reading on-chip fuse5 data:

Reading | ################################################## | 100% 0.00s

avrdude: verifying ...
avrdude: 1 bytes of fuse5 verified
avrdude: reading input file "0x00"
avrdude: writing fuse7 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse7 written
avrdude: verifying fuse7 memory against 0x00:
avrdude: load data fuse7 data from input file 0x00:
avrdude: input file 0x00 contains 1 bytes
avrdude: reading on-chip fuse7 data:

Reading | ################################################## | 100% 0.00s

avrdude: verifying ...
avrdude: 1 bytes of fuse7 verified
avrdude: reading input file "0x00"
avrdude: writing fuse8 (1 bytes):

Writing | ################################################## | 100% 0.02s

avrdude: 1 bytes of fuse8 written
avrdude: verifying fuse8 memory against 0x00:
avrdude: load data fuse8 data from input file 0x00:
avrdude: input file 0x00 contains 1 bytes
avrdude: reading on-chip fuse8 data:

Reading | ################################################## | 100% 0.01s

avrdude: verifying ...
avrdude: 1 bytes of fuse8 verified
avrdude: reading input file "C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_874061/SFRRanger_reader.ino.hex"
avrdude: writing flash (4150 bytes):

Writing | ################################################## | 100% 1.41s

avrdude: 4150 bytes of flash written
avrdude: verifying flash memory against C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_874061/SFRRanger_reader.ino.hex:
avrdude: load data flash data from input file C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_874061/SFRRanger_reader.ino.hex:
avrdude: input file C:\Users\IVANFE~1\AppData\Local\Temp\arduino_build_874061/SFRRanger_reader.ino.hex contains 4150 bytes
avrdude: reading on-chip flash data:

Reading | ################################################## | 100% 0.78s

avrdude: verifying ...
avrdude: 4150 bytes of flash verified

avrdude done.  Thank you.
```
### Notes
1.  Each of the sketches compiled and uploaded successfully to the AVR128DA48 board.  This concludes testing 
of the Wire2 examples within the Team 25 core.




