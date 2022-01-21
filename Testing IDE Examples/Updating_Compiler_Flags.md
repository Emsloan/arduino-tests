# Updating Compiler Flags

Update build.usb_flags in platforms.txt to update the IDE
Change what is included in the brackets. See last line in code snippet below.

```sh

tools.avrdude.bootloader.pattern="{cmd.path}" "-C{config.path}" {bootloader.verbose} -p{build.mcu} -c{protocol} {program.extra_params} "-Uflash:w:{runtime.platform.path}/bootloaders/{bootloader.file}:i" -Ulock:w:{bootloader.lock_bits}:m

tools.avrdude_remote.upload.pattern=/usr/bin/run-avrdude /tmp/sketch.hex {upload.verbose} -p{build.mcu}

tools.avrdude.upload.network_pattern="{network_cmd}" -address {serial.port} -port {upload.network.port} -sketch "{build.path}/{build.project_name}.hex" -upload {upload.network.endpoint_upload} -sync {upload.network.endpoint_sync} -reset {upload.network.endpoint_reset} -sync_exp {upload.network.sync_return}

# USB Default Flags
# Default blank usb manufacturer will be filled in at compile time
# - from numeric vendor ID, set to Unknown otherwise
build.usb_manufacturer="Unknown"
build.usb_flags=-DUSB_VID={build.vid} -DUSB_PID={build.pid} '-DUSB_MANUFACTURER={build.usb_manufacturer}' '-DUSB_PRODUCT={build.usb_product}'
```

Alternatively, it can be updated locally via boards.txt:

```sh
# This can be overridden in boards.txt
build.extra_flags=

# These can be overridden in platform.local.txt
compiler.c.extra_flags=
compiler.c.elf.extra_flags=
compiler.S.extra_flags=
compiler.cpp.extra_flags=
compiler.ar.extra_flags=
compiler.objcopy.eep.extra_flags=
compiler.elf2hex.extra_flags=
```

The compiler flags can also be overwritten from other platform config files:



| Config File | Link |
| ------ | ------ |
| boards.txt | [https://arduino.github.io/arduino-cli/latest/platform-specification/#boardstxt][PlDb] |
| boards.local.txt| [https://arduino.github.io/arduino-cli/latest/platform-specification/#boardslocaltxt][PlGh] |
| platform.local.txt | [https://arduino.github.io/arduino-cli/latest/platform-specification/#platformlocaltxt][PlGd] |
| global platform.txt | [https://arduino.github.io/arduino-cli/latest/platform-specification/#global-platformtxt][PlOd] |

You can also do it from the command line: --build-properties

This will override the value of the build.extra_flags property that could have been set in  boards.txt.

```sh
arduino-cli compile --fqbn arduino:avr:uno --build-properties build.extra_flags=-DFLAGNAME SketchName
```