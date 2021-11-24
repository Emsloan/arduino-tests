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
The next element within the a package is **platforms**. Platforms contains:

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


Thanksgiving Thanksgiving
