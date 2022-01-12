# How to create the JSON Index File

TODO

The JSON file allows for your platform to be installed and updated using the IDE's Boards Manager. The root level of the files consists of an array of **packages**.

```json
{
    "packages":[
    {
        //package goes here
    }
    
    ]
    
}
```

## Metadata
Each package has metadata used to construct the hardware file structure and display information within the Boards Manager. These include:
- **name** - used to name the vendor/maintainer folder (the highest level of the hardware folders)
- **maintainer** - the name displayed within the Boards Manager
- **websiteURL** - URL to the vendors webstie
- **email** - vendor/maintainer contact info
```json
{
    "packages":[
    {
        "name": "newboard",
        "maintainer": "John Doe",
        "websiteURL": "http://MyBoards.web/",
        "email": "jdoe@myboards.web",
    }
    ]
}
```
## Platforms
The next element within the package is **platforms**. Platforms contains:

- **name** - the platform name displayed in the Boards Manager
- **architecture** - the platform architecture TODO
- **version**
- **category** - set to Contributed 
- **help** - a URL displayed within the Boards Manager linking to help resources for this platform
- **url** - a link to the archive, what the Boards Manager actually downloads and installs
- **archiveFileName** - the name of the archive
- **checksum** - a hash value generated from the archive file
- **size** - the size of the archive
- **boards** - an array with the **name** of any boards within the package
- **toolsDependencies** - an array of any tools needed for this package. Each element in the array has **packager**, **name**, and **version**. See the later

```json
{
    "packages": [
    {
        "name": "newboard",
        "maintainer": "John Doe",
        "websiteURL": "http://MyBoards.web/",
        "email": "jdoe@myboard.web",
    },
    "platforms": [
        {
          "name": "New Board",
          "architecture": "avr",
          "version": "1.0.0",
          "category": "Contributed",
          "help": {
            "online": "http://MyBoards.web/help/newboard"
          },
          "url": "https://jdoe.github.io/newboard/newboard-1.0.0.zip",
          "archiveFileName": "newboard-1.0.0.zip",
          "checksum": "SHA-256:ec3ff8a1dc96d3ba6f432b9b837a35fd4174a34b3d2927de1d51010e8b94f9f1",
          "size": "20,001",
          "boards": [{ "name": "New Board" }],
          "toolsDependencies": [
            {
              "packager": "arduino",
              "name": "avr-gcc",
              "version": "4.8.1-arduino5"
            },
            {
              "packager": "arduino",
              "name": "avrdude",
              "version": "6.0.1-arduino5"
            }
          ]
        },
      ],
  ]
}
```

## Tools

The final element within a package is **tools**. Each element in tools corresponds to a CLI tool. Below is an example (taken from Arduino package index specification) of how the section might look in your package:
```json
{
          "name": "avr-gcc",
          "version": "7.3.0-atmel3.6.1-arduino7",
          "systems": [
            {
              "size": "34683056",
              "checksum": "SHA-256:3903553d035da59e33cff9941b857c3cb379cb0638105dfdf69c97f0acc8e7b5",
              "host": "arm-linux-gnueabihf",
              "archiveFileName": "avr-gcc-7.3.0-atmel3.6.1-arduino7-arm-linux-gnueabihf.tar.bz2",
              "url": "http://downloads.arduino.cc/tools/avr-gcc-7.3.0-atmel3.6.1-arduino7-arm-linux-gnueabihf.tar.bz2"
            },
            {
              "size": "38045723",
              "checksum": "SHA-256:03d322b9df6da17289e9e7c6233c34a8535d9c645c19efc772ba19e56914f339",
              "host": "aarch64-linux-gnu",
              "archiveFileName": "avr-gcc-7.3.0-atmel3.6.1-arduino7-aarch64-pc-linux-gnu.tar.bz2",
              "url": "http://downloads.arduino.cc/tools/avr-gcc-7.3.0-atmel3.6.1-arduino7-aarch64-pc-linux-gnu.tar.bz2"
            },
            {
              "size": "36684546",
              "checksum": "SHA-256:f6ed2346953fcf88df223469088633eb86de997fa27ece117fd1ef170d69c1f8",
              "host": "x86_64-apple-darwin14",
              "archiveFileName": "avr-gcc-7.3.0-atmel3.6.1-arduino7-x86_64-apple-darwin14.tar.bz2",
              "url": "http://downloads.arduino.cc/tools/avr-gcc-7.3.0-atmel3.6.1-arduino7-x86_64-apple-darwin14.tar.bz2"
            },
            {
              "size": "52519412",
              "checksum": "SHA-256:a54f64755fff4cb792a1495e5defdd789902a2a3503982e81b898299cf39800e",
              "host": "i686-mingw32",
              "archiveFileName": "avr-gcc-7.3.0-atmel3.6.1-arduino7-i686-w64-mingw32.zip",
              "url": "http://downloads.arduino.cc/tools/avr-gcc-7.3.0-atmel3.6.1-arduino7-i686-w64-mingw32.zip"
            },
            {
              "size": "37176991",
              "checksum": "SHA-256:954bbffb33545bcdcd473af993da2980bf32e8461ff55a18e0eebc7b2ef69a4c",
              "host": "i686-linux-gnu",
              "archiveFileName": "avr-gcc-7.3.0-atmel3.6.1-arduino7-i686-pc-linux-gnu.tar.bz2",
              "url": "http://downloads.arduino.cc/tools/avr-gcc-7.3.0-atmel3.6.1-arduino7-i686-pc-linux-gnu.tar.bz2"
            },
            {
              "size": "37630618",
              "checksum": "SHA-256:bd8c37f6952a2130ac9ee32c53f6a660feb79bee8353c8e289eb60fdcefed91e",
              "host": "x86_64-linux-gnu",
              "archiveFileName": "avr-gcc-7.3.0-atmel3.6.1-arduino7-x86_64-pc-linux-gnu.tar.bz2",
              "url": "http://downloads.arduino.cc/tools/avr-gcc-7.3.0-atmel3.6.1-arduino7-x86_64-pc-linux-gnu.tar.bz2"
            }
          ]
        }
```

- **name** - tool name
- **version** - tool version
- **systems** - an array with each element corresponding to the tool implentation for a given OS
    - **size** - the size of the archive
    - **checksum** - a hash value generated from the archive file
    - **host** - the name of the archive
    -  **archiveFileName** - the name of the ziped archive that contains the tool
    -  **url** - a link to the location of the archive to be downloaded
