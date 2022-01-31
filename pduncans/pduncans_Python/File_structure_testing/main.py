# The of this python script is to access the operating systems
# file structure to automate the process of uploading a sketch
# to  the AVR128DA48.  THis can be done through the command line
# using a python script, as shown below.  This program requires the
# location of avrdude on to function properly

import os

# Open file from file system and write it to a new file
# Read from file and output to a new file

# Create files for reading and writing
input_file = open("resource/second_lvl/input.txt", "r")
output_file = open("write_to_output.txt", "w")

# Write lines from input to output
for line in input_file:
    output_file.write(line)

# close resources
input_file.close()
output_file.close()

# Sketch upload
# Path to the avrdude uploader used to send a sketch to the board
path = ":C:/Users/paulm/AppData/Local/Arduino15/packages/arduino/tools/avrdude/6.3.0-arduino18/bin/avrdude -CC:/Users/paulm/AppData/Local/Arduino15/packages/Microchip/hardware/megaavr/1.0.0/avrdude.conf -v -pavr128da48 -ccuriosity_updi -Pusb -Ufuse5:w:0b11001001:m -Ufuse6:w:0x04:m -Ufuse7:w:0x00:m -Ufuse8:w:0x00:m"

# Sketch location that tests for the proper uploading of the Arduino sketch
test_file = " -Uflash:w:D:/Homework/Capstone/Tests/arduino-tests/pduncans_Python/File_structure_testing/blink_testing.ino.hex:i"

# Combine the path and file location
upload = path + test_file

# Direct the terminal information to a new text file
direct_output = " > output.txt 2>&1"

# Combine everything into one command
upload_output = upload + direct_output

os.system(upload_output)
