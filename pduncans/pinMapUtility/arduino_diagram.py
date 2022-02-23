# coding=utf-8

"""
Automatic SVG generator from XML or NET list.

This generetor can decode a PADS NET list and generate a XML and SVG.
This generator can decode a XML and generate a SVG.
"""
from __future__ import print_function
import sys
import math
import os
from collections import defaultdict
from xml.etree import ElementTree as ETree
from xml.dom import minidom
from svgwrite import Drawing
from svgwrite import shapes as svg_shapes
from svgwrite import path as svg_path
from svgwrite import text as svg_text
from svgwrite import cm


# Microchip logo vector string
LOGO = "m 262.58708,236.59626 c 6.50295,0 11.38016,5.28365 11.38016,11.7866 " \
       "0,6.09651 -4.87721,11.78659 -11.38016,11.78659 -6.50295,0 -11.38015," \
       "-5.28365 -11.38015,-11.78659 0,-6.50295 4.8772,-11.7866 11.38015,-11" \
       ".7866 z m -9.75442,11.7866 c 0,5.28364 4.06434,9.34798 9.75442,9.347" \
       "98 5.28364,0 9.75442,-4.06434 9.75442,-9.34798 0,-5.28365 -4.06434,-" \
       "9.34799 -9.75442,-9.34799 -5.69008,-0.40644 -9.75442,4.06434 -9.7544" \
       "2,9.34799 z m 3.25147,-2.43861 v -2.03217 h 13.41233 v 4.87721 c 0,3" \
       ".25147 -1.2193,4.87721 -3.65791,4.87721 -2.4386,0 -3.25147,-1.62574 " \
       "-3.6579,-3.25147 l -5.69008,3.65791 v -2.43861 l 5.69008,-3.65791 v " \
       "-2.4386 h -6.09652 z m 7.31582,2.03217 c 0,1.62574 0,3.25148 2.03217" \
       ",3.25148 1.62574,0 2.03217,-1.62574 2.03217,-2.84504 v -2.84504 h -4" \
       ".06434 z m 6.90938,-36.17264 c 8.94156,-19.10241 13.41233,-36.98552 " \
       "13.81877,-59.74584 1.62573,-82.506148 -60.96514,-150.7870981 -139.40" \
       "695,-152.00640806 -13.41233,-0.40643 -26.82465,1.62573996 -39.42411," \
       "4.87721996 l 59.74582,42.6755901 -45.1142,28.85684 c 0,0 -9.75441,8." \
       "53511 -19.91527,2.03216 -0.812869,-0.40643 -54.055749,-39.01768 -54." \
       "055749,-39.01768 -28.04396,26.82466 -45.11419346,64.623048 -45.92706" \
       "246,107.298638 -0.812869,41.86272 14.63163246,78.84824 40.23699246,1" \
       "06.48577 l 143.471269,-90.63484 c 0,0 19.91528,14.2252 36.17265,25.6" \
       "0536 17.47667,12.19303 5.28364,23.57319 -0.40644,27.23109 -41.86273," \
       "26.41823 -120.710969,76.40964 -120.710969,76.40964 h 0.40644 c 11.78" \
       "6589,5.28364 15.444499,7.72225 32.108299,8.12868 z m -171.515249,-21" \
       ".54102 c 0,0 -35.35977,-23.97962 -38.61125,-26.82466 -19.91526,-14.6" \
       "3163 3.25148,-25.60536 3.25148,-25.60536 l 120.710959,-76.816068 c 0" \
       ",0 19.91528,14.2252 36.17265,25.60536 17.47667,12.19302 5.28364,23.5" \
       "73188 -0.40643,27.231088 -42.26917,26.82466 -121.117409,76.40964 -12" \
       "1.117409,76.40964 z"

MBUS = "m 461.8,99.89 c -14.8,0.61 -29.9,-1.4 -44.6,1.31 -13.3,11.2 5.5,18.6" \
       " 15.9,15.9 11.7,0 28.3,-1.7 31.5,13.2 5.4,15.7 -8,31.6 -24.5,28.7 -1" \
       "3.4,0 -26.9,0 -40.4,0 1.2,-4.8 -3.6,-15.5 5,-13 13.8,-0.6 28.1,1.6 4" \
       "1.7,-1.6 10.5,-12.2 -7.9,-16.7 -17.6,-14.7 -11.5,0.3 -27.6,0.4 -31.2" \
       ",-13.4 -5.6,-15.8 7.7,-32.36 24.4,-29.37 13.3,0 26.5,0 39.8,0 0,4.32" \
       " 0,8.64 0,12.96 z m -123,-12.96 c 0.9,17.77 -1.3,35.87 1.3,53.37 8.8" \
       ",16.5 37.1,5.9 31,-13 0,-13.5 0,-26.9 0,-40.37 4.5,1.53 15.4,-3.35 1" \
       "5,2.97 -0.4,18 1.2,36.2 -1.2,54 -5.8,17.1 -28.1,17.5 -43,14.4 -17.2," \
       "-2.4 -19.5,-20.6 -18.1,-34.6 0,-12.3 0,-24.51 0,-36.77 4.9,0 10,0 15" \
       ",0 z m -53.3,59.27 c 19.3,-1.6 5.7,-22.4 -7.9,-16.9 -4.6,1.4 -15.8,-" \
       "3.7 -14.5,3.9 1.2,4.9 -3.5,15.5 5.1,13 5.7,0 11.6,0 17.3,0 z m -22.4" \
       ",-46.31 c 1.2,5.01 -2.4,14.81 2,16.61 9.2,-0.6 18.9,1.7 27.6,-1.8 9." \
       "6,-14.2 -9.5,-16.13 -19.3,-14.81 -3.5,0 -6.8,0 -10.3,0 z m 24.5,59.1" \
       "1 c -13.2,0 -26.4,0 -39.6,0 0,-24 0,-48 0,-72.07 17.9,0.77 36.2,-2.0" \
       "5 53.5,2.59 13.9,5.66 13.1,27.88 -0.9,33.48 20,7.5 10.1,39.6 -10.6,3" \
       "5.8 z m 153.3,-105.51 c 32.9,2.81 -0.9,-47.512 -7.1,-12.16 0,4.84 2." \
       "2,10.4 7.1,12.16 z m 19.9,3.9 c -12.6,11.96 -38.1,4.94 -38.4,-13.83 " \
       "-2.5,-15.78 14.4,-28.25 28.9,-23.31 16.5,3.4 20.5,26.06 9.5,37.14 z " \
       "m -73.3,-37.14 c 9.4,0.93 20.4,-2.4 28.5,3.16 6.8,9.5 -0.4,18.76 -8." \
       "7,13.45 4.2,-9.88 -13,-12.43 -8.8,-1.61 0,9.05 0,18.11 0,27.14 -6,0 " \
       "-13.8,1.96 -11,-6.93 0,-11.74 0,-23.5 0,-35.21 z m -47.8,-19.6023 c " \
       "6,0 13.9,-1.9997 11.1,6.9303 0,10.932 0,21.962 0,32.922 6,-6.75 12,-" \
       "13.52 18,-20.25 3.5,1.05 18.1,-2.67 11.3,2.84 -5.6,5.9 -11.2,11.82 -" \
       "16.9,17.73 6.5,7.19 13.1,14.37 19.6,21.57 -5.5,-1.18 -13.2,2.59 -16." \
       "9,-2.28 -5,-6.06 -10.2,-12.13 -15.1,-18.19 0,6.82 0,13.65 0,20.47 -6" \
       ".1,0 -14,1.95 -11.1,-6.93 0,-18.28 0,-36.55 0,-54.8123 z m -9.9,61.7" \
       "423 c -6.2,0 -14.6,2.08 -11.6,-6.92 0,-11.75 0,-23.51 0,-35.22 6.1,0" \
       " 14.4,-2.14 11.6,6.89 0,11.75 0,23.51 0,35.25 z m 0,-51.34 c -6.2,0 " \
       "-14.6,2.13 -11.6,-6.932 -2.4,-5.6 13.2,-5.2 11.6,-0.54 0,2.54 0,5.07" \
       " 0,7.472 z m -81.8,9.2 c 16.7,0.45 33.5,-1.07 50.2,0.84 13.6,3.41 9." \
       "3,19.12 10,29.47 -1,5.3 2.9,14.78 -5.9,11.86 -8.7,2.58 -4.1,-7.93 -5" \
       ".3,-12.85 1,-9.65 1.4,-24.61 -13.4,-19.95 0,10.92 0,21.87 0,32.8 -6." \
       "1,0 -14.2,2.04 -11.3,-6.92 0,-8.63 0,-17.25 0,-25.88 -4.9,1.19 -15.6" \
       ",-3.52 -13.2,4.94 0,9.29 0,18.58 0,27.86 -6.1,0 -13.9,1.96 -11.1,-6." \
       "92 0,-11.76 0,-23.5 0,-35.25 z m -42.5,58.59 c -15.2,0 -30.2,0 -45.4" \
       ",0 0,-11.4 0,-22.79 0,-34.2 19.6,-1.99 24.2,-31.33 6.8,-39.592 -14.7" \
       ",-8.93 -35,5.732 -31.1,22.472 1.2,15.08 22.4,13.09 17.2,28.94 0,7.46" \
       " 0,14.92 0,22.38 -27.8,0 -55.55,0 -83.38,0 0,-11.4 0,-22.79 0,-34.2 " \
       "19.62,-1.98 24.25,-31.33 6.77,-39.592 -14.6,-8.93 -34.91,5.732 -30.9" \
       "4,22.472 1.05,15.08 22.33,13.09 17.12,28.94 0,7.46 0,14.92 0,22.38 -" \
       "15.09,0 -30.27,0 -45.35,0 0,13.78 0,27.56 0,41.36 -19.335,2.3 -23.68" \
       ",31.2 -6.38,39.4 14.7,9 35,-5.8 31.03,-22.5 -1.07,-15.2 -22.81,-12.8" \
       " -17.49,-28.8 0,-7.5 0,-14.95 0,-22.4 27.84,0 55.67,0 83.52,0 0,11.4" \
       "3 0,22.8 0,34.3 -19.34,2.3 -23.69,31.2 -6.4,39.4 14.7,9 35,-5.8 31,-" \
       "22.5 -1.1,-15.2 -22.8,-12.8 -17.5,-28.8 0,-7.5 0,-14.95 0,-22.4 27.8" \
       ",0 55.6,0 83.5,0 0,11.43 0,22.8 0,34.3 -19.5,2.2 -23.8,31.2 -6.6,39." \
       "4 14.7,9 35.1,-5.8 31.1,-22.5 -1.1,-15.2 -22.8,-12.8 -17.5,-28.8 0,-" \
       "9.85 0,-19.65 0,-29.46 z"

MBUS_OUTLINE = 'm 100 0 a 100,100 0 0,0 -100,100 v 925 a 100,100 0 0,0 100,100 h 900 a 100,100 0 0,0 100,-100 ' \
               'v -925 a 100,100 0 0,0 -100,-100 m -950 175 h 100 v 800 h -100 v -800 m 0 100 h 100 m 800 -100' \
               ' h 100 v 800 h -100 v -800 m 0 100 h 100 m 0 700 l -100 100'
XPRO_OUTLINE = 'm 450 75 h 200 v 1000 h -200 v -1000'

# Used for parsing Altium net lists. This is the designator for the CNANO edge connector.
EDGE_DESIGNATOR = "J200"

# Below what color lightness level should white text be used?
TEXTBOX_LIGHTNESS_THRESHOLD = 120

# This defines which pin labels are color coded by category and included in the legend.
#   Category   Edge    Fill       Legend
PIN_TYPES = {
    "ANALOG": ['none', '#7BB81E', "Analog", 1],
    "DEBUG":  ['none', '#0070C0', "Debug", 2],
    "I2C":    ['none', '#6659C1', "I2C", 3],
    "SPI":    ['none', '#D8CC91', "SPI", 4],
    "UART":   ['none', '#00B0F0', "UART", 5],
    "PER":    ['none', '#CC7212', "Peripheral", 6],
    "PORT":   ['none', '#A5A5A5', "Port", 7],
    "TIMER":  ['none', '#424242', "PWM", 8],
    "POWER":  ['none', '#FF0000', "Power", 9],
    "GND":    ['none', '#000000', "Ground", 10],
    "MVIO":   ['none', '#F7B400', "MVIO", 11],
    "OPAMP":  ['none', '#009900', "OPAMP", 12],
    "ARDUINO":['none', '#119E94', "ARDUINO", 13],
    "CAN":    ['none', '#ABCDEF', "CAN", 14],
    "USB":    ['none', '#B200FF', "USB", 15],
    "PPS":    ['none', '#0CFF00', "PPS", 16],
    "SHARED": ['#ED1B2E', 'none', "Shared pin", 17]
}


# arduino teal '#119E94'
# touch biege '#D8CC91'



FONTS = {
    "label":     "Lucida Console",
    "pin":       "Arial Rounded MT Bold",
    "component": "Arial Rounded MT Bold",
    "kit_name":  "Arial Rounded MT Bold"
}

COLORS = {
    # What      Edge color   Fill color  Stroke width
    "outline": ['black', '#ED1B2E', 5],
    "hole_lines": ['#ff9900', 'none', 15],
    "holes": ['#ff9900', 'white', 15],
    "origin": ['black', 'red', 2],
    "components": ['black', '#555555', 2],
}

LABELS_LEFT = ["AN", "RST", "CS", "SCK", "MISO", "MOSI", "+3.3V", "GND"]
LABELS_RIGHT = ["PWM", "INT", "RX", "TX", "SCL", "SDA", "+5V", "GND"]


def get_pin_type(text):
    """
    Solves the pin type of the pin based on name
    :param text: Pin name
    :return: The category of the pin. Defaults to PORT.
    """
    pin_type = "PORT"
    text = text.strip().upper()
    if any(txt in text for txt in ("CDC", "UART", "RX", "TX")):
        pin_type = "UART"
    if any(txt in text for txt in ("I2C", "SDA", "SCL")):
        pin_type = "I2C"
    if any(txt in text for txt in ("SPI", "MOSI", "MISO", "SCK", "SS", "CS")):
        pin_type = "SPI"
    if any(txt in text for txt in ("AD", "AN", "AIN")):
        pin_type = "ANALOG"
    if any(txt in text for txt in ("LED", "SW", "TOSC", "SOSC", "BTN")):
        pin_type = "PER"
    if any(txt in text for txt in ("TC", "PWM")):
        pin_type = "TIMER"
    if any(txt in text for txt in ("VCC", "VTG", "VBUS")):
        pin_type = "POWER"
    if "GND" in text:
        pin_type = "GND"
    if any(txt in text for txt in ("DBG", "ICSP", "PDI", "SWD", "ID", "MCLR", "RST", "RESET")):
        pin_type = "DEBUG"
    return pin_type


# Takes in filename for a PADS ASCII Netlist from Altium, returns dictionary based on the nets connected
# to EDGE_DESIGNATOR with {pin_number: net_name}
def netlist_to_pin_out(name):
    """
    Converts a NET list to xml output
    :param name: Filename of net list
    :return: XML string list
    """
    with open(name, "r") as f_ptr:  # Open file, close on scope exit
        lines = f_ptr.read().split("\n")

    pin_out = defaultdict(list)
    signal = ""
    for line in lines:
        if line.startswith("*SIGNAL*"):
            signal = line.split(' ')[1]
        if not line.startswith("*"):
            pin_out[signal] += line.strip().split(' ')

    pin_out_list2 = {1: ['NC', '']}
    for pin in range(2, 60):
        search_str = "{}.{}".format(EDGE_DESIGNATOR, pin)
        for net in pin_out:
            if search_str in pin_out[net]:
                pin_out_list2[pin] = [net, pin_out[net]]

    # for x in pin_out_list2:
    #    print(x, pin_out_list2[x])

    pin_out_list = {1: ['NC', '']}
    pin_found = True
    pin_number = 2
    # Find all pins documented in net list. MAY TERMINATE PREMATURELY ON PIN NOT ASSIGNED TO NET.
    while pin_found:
        pin_found = False
        for index, line in enumerate(lines):
            search_str = "{}.{} ".format(EDGE_DESIGNATOR, pin_number)
            if search_str in "{} ".format(line):
                pin_found = True
                iterator = index
                while 1:  # Iterate backwards and look for *SIGNAL* <net name>
                    iterator -= 1
                    assert iterator >= 0, "Net list file broken, *SIGNAL* line not found ahead of pin"

                    if "*SIGNAL*" in lines[iterator]:  # Does line contain net name?
                        pin_out_list.update({pin_number: [(lines[iterator].split(' '))[1]]})
                        pin_out_list[pin_number].append(lines[iterator+1].replace(search_str, ''))
                        break
                # print "Pin found: {}.{} {}".format(EDGE_DESIGNATOR, pin_number, (lines[iterator].split(' '))[1])
                pin_number += 1

    # for x in pin_out_list:
    #    print(x, pin_out_list[x])

    # Find the connection on the cut-straps
    for item in pin_out_list:
        if ("DBG" in pin_out_list[item][0]) or ("CDC" in pin_out_list[item][0]):
            connection = pin_out_list[item][1].split(' ')
            for conn in connection:
                if "J20" in conn:
                    part, pin = conn.split('.')
                    part_pin = "{}.{}".format(part, 2)
                    if pin == '2':
                        part_pin = "{}.{}".format(part, 1)
                    for num, line in enumerate(lines, start=0):
                        if part_pin in line:
                            pin_out_list[item][0] = pin_out_list[item][0] + '_' + lines[num-1].split(' ')[1]
                            break

    # for x in pin_out_list:
    #     print(x, pin_out_list[x])

    # print "Pin number {} not found. Terminating.".format(pin_number)
    print("{} pins found..".format(pin_number - 1))

    top = ETree.Element("pinout", device=os.path.basename(name).split('_')[0])
    for items in pin_out_list:
        child = ETree.SubElement(top, 'pin', {'id': "pin{}".format(items)})
        pin_out_list[items][0] = pin_out_list[items][0].replace('CDC_TX', 'CDC TX')
        pin_out_list[items][0] = pin_out_list[items][0].replace('CDC_RX', 'CDC RX')
        pin_out_list[items][0] = pin_out_list[items][0].replace('VCC_TARGET', 'VTG')
        pin_out_list[items][0] = pin_out_list[items][0].replace('ID_SYS', 'ID')
        split_list = pin_out_list[items][0].split('_')
        for entity in split_list:
            label = entity.replace('\\', '')
            ETree.SubElement(child, 'function', {'label': label, 'category': get_pin_type(label)})

    xml_str_list = minidom.parseString(ETree.tostring(top)).toprettyxml(indent="  ", encoding="utf-8")

    return xml_str_list


def get_label_color(category):
    """
    Get the color for the given category.
    :param category: category for the pin
    :return: the color for the category. Dull grey if no defined category.
    """
    string = category.upper()
    for identifier in PIN_TYPES:
        if string == identifier:
            return PIN_TYPES[identifier][1]

    return '#e6e6e6'  # Dull grey is fine for unspecified labels


def get_lightness(color):
    """
    Get lightness of a color
    :param color: input colot
    :return: lightness of the color
    """
    red = int((color[1] + color[2]), 16)
    green = int((color[3] + color[4]), 16)
    blue = int((color[5] + color[6]), 16)

    # Luma calculation based on CCIR 601
    luma = (0.299*red) + (0.587*green) + (0.114*blue)

    return luma


def calculate_max_box_width(pin_out_list):
    """
    Calculate the maximum box width for the complete SVG
    :param pin_out_list: List with names of pin out
    :return: Maximum box width
    """
    character_width = 36.3

    max_letters = 0

    for pin in pin_out_list:
        for pin_func in pin:
            if len(pin_func.attrib['label']) > max_letters:
                max_letters = len(pin_func.attrib['label'])

    return int(max_letters * character_width) + 80  # Add end radii

def vector_rotate(vector, angle):
    """
    Performs 2D vector roation in the clockwise direction with a standard
    rotation matrix
    :param vector: 2D vector i.e. a pair of points x and y
    :param angle: angle in radians specifying clockwise rotation
    """
    vector_x = vector[0]
    vector_y = vector[1]
    vector[0] = vector_x * math.cos(angle) - vector_y * math.sin(angle)
    vector[1] = vector_x * math.sin(angle) + vector_y * math.cos(angle)

    return vector

def transform_svg_string(svg_string, scale, rotation):
    """
    Scales and rotates the specified vector string
    :param logo: vector string
    :param scale: scaling factor
    :param rotation: clockwise rotation specified in radians
    """

    # Decompose the vector string into its subcomponentes, so it is easier to
    # scale the numbers
    space_fragments = svg_string.split()
    logo_vector = []
    for frag in space_fragments:
        if frag.find(','):
            comma_fragments = frag.split(',')
            logo_vector.append(comma_fragments)
        else:
            logo_vector.append(frag)

    # Go through all the items in the SVG string. Every number will be scaled
    for i in range(len(logo_vector)):

        # Since we are doing 2D rotation we cannot user SVGs 'v' and 'h' tags
        # since they are 1-dimentional
        if logo_vector[i][0] == 'h':
            logo_vector[i][0] = 'l'
            logo_vector[i + 1].append('0.0')
        if logo_vector[i][0] == 'v':
            logo_vector[i][0] = 'l'
            tmp = logo_vector[i + 1][0]
            logo_vector[i + 1][0] = '0.0'
            logo_vector[i + 1].append(tmp)

        # Perform vector rotation on number pairs
        if len(logo_vector[i]) == 2:
            try:
                vector = []
                vector.append(float(logo_vector[i][0]))
                vector.append(float(logo_vector[i][1]))

                vector = vector_rotate(vector, rotation)
                
                logo_vector[i][0] = str(vector[0])
                logo_vector[i][1] = str(vector[1])
            except ValueError:
                pass
        
        # Scale all vectors
        for j in range(len(logo_vector[i])):
            try:
                vector_number = float(logo_vector[i][j])
                vector_number *= scale
                logo_vector[i][j] = str(vector_number)
            except ValueError:
                pass

    # Re-assemble the SVG vector string
    new_svg_string = ""
    for vector in logo_vector:
        if len(vector) > 1:
            new_svg_string += ", ".join(vector)
        else:
            new_svg_string += vector[0]
        new_svg_string += " "
    
    return new_svg_string

def cnano(name, pin_out):    
    """
    Convert the pin out to SVG

    Outline for CNANO:

       width
     _________
    |   usb   |
    |         | l
    |         | e
    |         | n
    |         | g
    |         | t
    |         | h
    |_________|

    :param name: File name of the output SVG
    :param pin_out: XML input for parsing
    """
    # Get the package type and shape
    package_type = ""
    for pin in pin_out:
        if (pin.tag == 'package'):
            package_type = str(pin.attrib['type'])
            pin_out.remove(pin)
            break
    number_of_pins = len(pin_out)

    if number_of_pins % 2:
        raise ValueError("Odd number of pins defined")

    number_of_rows = int(number_of_pins / 2)
    svg_width = 15  # in cm
    px_pr_cm = 37.795

    # Size of the board
    length = 500 + number_of_rows * 100
    width = 800

    text_origin_x = 250
    hole_r = 25  # hole radius
    text_box_width = calculate_max_box_width(pin_out)

    target_chip_radius = number_of_pins * 3  # Aesthetic parameter

    dwg = Drawing(filename=name, size=(svg_width, svg_width))

    # Create layers for the drawing, first layer = bottom layer
    outline = dwg.add(dwg.g(id='outline', stroke=COLORS['outline'][0], fill=COLORS['outline'][1],
                            stroke_width=COLORS['outline'][2]))
    hole_lines = dwg.add(dwg.g(id='hole_lines', stroke=COLORS['hole_lines'][0], fill=COLORS['hole_lines'][1],
                               stroke_width=COLORS['hole_lines'][2]))
    holes = dwg.add(dwg.g(id='holes', stroke=COLORS['holes'][0], fill=COLORS['holes'][1],
                          stroke_width=COLORS['holes'][2]))
    components = dwg.add(dwg.g(id='components', stroke=COLORS['components'][0], fill=COLORS['components'][1],
                               stroke_width=COLORS['components'][2]))

    # Pin label and legend layers
    text_boxes = dwg.add(dwg.g(id='text_boxes', stroke_width='2'))
    text = dwg.add(dwg.g(id='text'))

    # Legend
    legend = dwg.add(dwg.g(id='legend', stroke_width='2'))

    # Determine board position
    max_labels = 0
    for pin in pin_out:
        count = len(pin)
        if count > max_labels:
            max_labels = count

    # Determine which functions are used
    used_functions = set(['SHARED'])
    for pin in pin_out:
        for pin_func in pin:
            used_functions.update([pin_func.attrib['category']])

    # Upper left corner of the board, x-coordinate must be computed first
    board_origin_x = text_origin_x + (text_box_width + 20) * max_labels

    # Add legend
    legend_origin_x = board_origin_x + 960
    legend_origin_y = 200
    legend_end_y = legend_origin_y

    row_count = 0

    # Only show legend for pin types in use
    used_types = {k: PIN_TYPES[k] for k in used_functions}

    for identifier in sorted(used_types.items(), key=lambda x: (x[1][3], x[0])):
        legend.add(svg_shapes.Rect(
            insert=(legend_origin_x, legend_end_y),
            size=(80, 80),
            rx=40, ry=40, stroke=identifier[1][0], fill=identifier[1][1], stroke_width=5
        ))

        legend.add(svg_text.Text(
            str(identifier[1][2]),
            insert=(legend_origin_x + 150, legend_end_y + 60),
            font_family=FONTS['label'], font_size=60
        ))
        row_count += 1
        legend_end_y += 100
        if row_count > 5:
            row_count = 0
            legend_end_y = legend_origin_y
            legend_origin_x += 600

    # Upper left corner of the board, y-coordinate
    board_origin_y = legend_origin_y + 400

    # origin.add(dwg.circle(center=(board_origin_x, board_origin_y), r=10))

    # Coordinates for on-board things
    x_1 = board_origin_x + 100  # x-coordinate for left mounting holes and pin holes
    y_1 = board_origin_y + 100  # y-coordinate for upper mounting holes
    x_2 = x_1 + 600  # x-coordinate for right mounting holes and pin holes
    y_2 = y_1  # y-coordinate for upper mounting holes

    x_3 = x_1  # x-coordinate for mounting holes and pin holes
    y_3 = board_origin_y + length - 100  # y-coordinate for lower mounting holes
    x_4 = x_2  # x-coordinate for  right mounting holes and pin holes
    y_4 = y_3  # y-coordinate for lower mounting holes

    x_text_left = x_1 - 300 - (text_box_width - 80)  # x-coordinate for origin of first label text on  left side
    x_text_right = x_2 + 300  # y-coordinate for origin of first label text on right side

    y_p = y_1 + 200  # y-coordinate for upper pin hole

    start = "{} {}".format(board_origin_x, board_origin_y)

    # Draw the board outline:
    line_p = svg_path.Path('M{}'.format(start))

    # Upper edge
    line_p.push('m 100 0')
    line_p.push('h {}'.format(width - 200))
    line_p.push('a 100,100 0 0,1 100,100')

    # Right-hand-side-squiggly-lines
    line_p.push('v {}'.format(200 - hole_r))
    for i in range(number_of_rows):
        line_p.push('a {}, {}, 0 0,0 0, {}'.format(hole_r, hole_r, hole_r * 2))
        line_p.push('v {}'.format(100 - hole_r * 2))
    line_p.push('v {}'.format(100 + hole_r))

    # Bottom edge
    line_p.push('a 100,100 0 0,1 -100,100')
    line_p.push('h -{}'.format(width - 200))
    line_p.push('a 100,100 0 0,1 -100,-100')

    # Left-hand-side-squiggly-lines
    line_p.push('v -{}'.format(200 - hole_r))
    for i in range(number_of_rows):
        line_p.push('a {}, {}, 0 0,0 0, -{}'.format(hole_r, hole_r, hole_r * 2))
        line_p.push('v -{}'.format(100 - hole_r * 2))
    line_p.push('v -{}'.format(100 + hole_r))

    line_p.push('a 100,100 0 0,1 100,-100')

    outline.add(line_p)

    # Add mounting holes
    holes.add(dwg.circle(center=(x_1, y_1), r=70))
    holes.add(dwg.circle(center=(x_2, y_2), r=70))
    holes.add(dwg.circle(center=(x_3, y_3), r=70))
    holes.add(dwg.circle(center=(x_4, y_4), r=70))

    # Add strap holes
    for pin in range(0, 6):
        holes.add(dwg.circle(center=(board_origin_x + 250 + 50 * pin, board_origin_y + 950), stroke_width=7, r=14))

    # Add power measurement holes
    holes.add(dwg.circle(center=(board_origin_x + 567, board_origin_y + 1000), r=30))
    holes.add(dwg.circle(center=(board_origin_x + 567, board_origin_y + 1100), r=30))
    hole_lines.add(dwg.line(start=(board_origin_x + 567, board_origin_y + 1000),
                            end=(board_origin_x + 567, board_origin_y + 1100)))

    # Keep track of the zigzag offset
    zigzag = 8

    # Add pin holes:
    for i in range(number_of_rows):
        y_i = y_p + i * 100
        holes.add(dwg.circle(center=(x_1 - zigzag, y_i), r=hole_r))
        holes.add(dwg.circle(center=(x_2 + zigzag, y_i), r=hole_r))
        hole_lines.add(dwg.line(start=(board_origin_x + hole_r, y_i), end=(x_1, y_i)))
        hole_lines.add(dwg.line(start=(x_2, y_i), end=(x_2 + 100 - hole_r, y_i)))
        zigzag *= -1

    # Add components for aesthetics/orientation
    # USB connector
    components.add(svg_shapes.Rect(insert=(board_origin_x + 241, board_origin_y - 18), size=(318, 225)))
    text.add(svg_text.Text(str("USB"), insert=(board_origin_x + width/2, board_origin_y + 104),
                           stroke='none',
                           fill="white",
                           font_family=FONTS['component'],
                           font_size=50,
                           text_anchor="middle"))
    # Debugger chip
    components.add(svg_shapes.Rect(insert=(board_origin_x + 223, board_origin_y + 418), size=(196, 196)))
    text.add(svg_text.Text(str("DEBUGGER"), insert=(board_origin_x + 223 + 196/2, board_origin_y + 418 + 113),
                           stroke='none',
                           fill="white",
                           font_family=FONTS['component'],
                           font_size=30,
                           text_anchor="middle"))

    # Button:
    button_size = 244
    button_x = board_origin_x + width / 2 - button_size/2
    button_y = board_origin_y + length - button_size - 13
    components.add(svg_shapes.Rect(insert=(button_x, button_y), size=(button_size, button_size)))
    components.add(dwg.circle(center=(button_x + button_size/2, button_y + button_size/2), fill="white", r=60))
    text.add(svg_text.Text(str("SW0"), insert=(board_origin_x + width/2, button_y - 10),
                           stroke='none',
                           fill="white",
                           font_family=FONTS['component'],
                           font_size=50,
                           text_anchor="middle"))
    # User LED:
    led_size = 30
    user_led_x = board_origin_x + width/2 - led_size
    user_led_y = board_origin_y + length - 394
    components.add(svg_shapes.Rect(insert=(user_led_x, user_led_y),
                                   size=(led_size*2, led_size), fill="#FFDD32"))
    text.add(svg_text.Text(str("LED0"), insert=(board_origin_x + width/2, board_origin_y + length - 394 - 10),
                           stroke='none',
                           fill="white",
                           font_family=FONTS['component'],
                           font_size=50,
                           text_anchor="middle"))

    # PS LED
    components.add(svg_shapes.Rect(insert=(board_origin_x + 169, board_origin_y + 239),
                                   size=(led_size, led_size*2), fill="#4FFF0F"))
    text.add(svg_text.Text(str("PS LED"), insert=(board_origin_x + 210, board_origin_y + 280),
                           stroke='none',
                           fill="white",
                           font_family=FONTS['component'],
                           font_size=50))

    # Draw the board logo:
    logo_x = board_origin_x + 280
    logo_y = board_origin_y + 1170
    start_logo = "{},{}".format(logo_x, logo_y)
    
    # Orientate the logo. The default is Microchip logo rotated pi/2 to the right
    new_logo = transform_svg_string(LOGO, 0.6, -math.pi / 2)
    components.add(svg_path.Path('M{} {}'.format(start_logo, new_logo), fill="white", stroke="none"))

    # Target chip
    lower_limit = user_led_y - 60
    upper_limit = logo_y + 10
    chip_offset = upper_limit + (lower_limit - upper_limit) / 2 - board_origin_y

    # These variables will determine the shape and rotation of the MCU
    rotate_mcu = 0
    target_chip_radius_x = number_of_pins
    target_chip_radius_y = number_of_pins
    chip_vector = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

    # If no package type is specified, QFN is assumed
    if package_type == "":
        package_type = "QFN"

    # Check the package type and scale the chip
    if package_type == "QFN":
        rotate_mcu = 1
        target_chip_radius_x *= 2
        target_chip_radius_y *= 2
    elif package_type == "TQFP":
        rotate_mcu = 1
        target_chip_radius_x *= 2.5
        target_chip_radius_y *= 2.5
    elif package_type == "TSSOP":
        # 1.3 due to the somewhat larger pitch on TSSOP
        # 1.5 to make the MCU rectangular
        target_chip_radius_x *= 3 / 1.5
        target_chip_radius_y *= 3
    elif package_type == "DIP":
        target_chip_radius_x *= 1
        target_chip_radius_y *= 4

    # Scale the unity size chip vector
    for point in chip_vector:
        point[0] *= target_chip_radius_x
        point[1] *= target_chip_radius_y

    # Rotate the chip if neseccary
    if rotate_mcu == 1:
        for i in range(len(chip_vector)):
            chip_vector[i] = vector_rotate(chip_vector[i], math.pi/4)   

    # Distance from MCU origin to the edge
    mcu_origin_edge = 0
    for point in chip_vector:
        for x in point:
            if x > mcu_origin_edge:
                mcu_origin_edge = x

    # Check if the MCU size is not to big, and scale the MCU if neseccary
    mcu_space_y = (lower_limit - upper_limit) / 2
    if mcu_origin_edge > mcu_space_y:
        print("Warning: chip is to big and will be scaled down to fit")
        scale = mcu_space_y / mcu_origin_edge
        for point in chip_vector:
            point_prev = point
            point[0] = point_prev[0] * scale
            point[1] = point_prev[1] * scale

    # Draw MCU and MCU name
    components.add(svg_shapes.Polygon(points=[(board_origin_x + width / 2 + p[0], board_origin_y + chip_offset + p[1]) for p in chip_vector]))
    text.add(svg_text.Text(str(pin_out.attrib["device"]),
                           insert=(board_origin_x + width/2, board_origin_y + chip_offset + target_chip_radius/16),
                           stroke='none',
                           fill="white",
                           font_family=FONTS['component'],
                           font_size=target_chip_radius/4,
                           text_anchor="middle"))

    # Reset the zigzag polarity
    if zigzag < 0:
        zigzag *= -1

    # Add pin out labels
    # Left/first row
    for pin in range(number_of_rows):
        color = get_label_color(pin_out[pin][0].attrib['category'])

        # Lines to labels
        if pin_out[pin][0].attrib['label'] != "":
            text_boxes.add(svg_shapes.Rect(
                insert=(x_text_left, y_p - 5 + pin * 100),
                size=(board_origin_x - x_text_left + 5, 10),
                rx=5, ry=5, stroke=color, fill=color
            ))

        label_offset = 0

        for functions in pin_out[pin]:
            color = get_label_color(functions.attrib['category'])

            # "silkscreen" pin labels on the board
            if label_offset == 0:
                # Check if the pin is NC
                cnano_pin_label = ""
                if str(functions.attrib['label']) == "":
                    cnano_pin_label = "NC"
                else:
                    cnano_pin_label = str(functions.attrib['label'])

                # text_center = (len(functions.attrib['label'].replace(' ', '')) * 18.2) / 2
                text.add(svg_text.Text(
                    cnano_pin_label,
                    insert=(board_origin_x + 145 + 10 - (zigzag*1.5), y_p + pin * 100),
                    stroke="none", fill="white", font_family=FONTS['pin'], font_size=30,
                    glyph_orientation_vertical=90, writing_mode="tb", text_anchor="middle"
                ))
                zigzag *= -1

                # If the pin is NC this functions should break
                if str(functions.attrib['label']) == "":
                    break

            if get_lightness(color) > TEXTBOX_LIGHTNESS_THRESHOLD:  # Should use black text?
                text_color = '#000000'
            else:
                text_color = '#FFFFFF'

            stroke_color = color
            if functions.attrib['category'] in ["PORT", "MVIO"]:
                if len(ROOT.findall(".//*[@label='{}']".format(functions.attrib['label']))) > 1:
                    if functions.attrib['label'] != 'NC':
                        stroke_color = PIN_TYPES['SHARED'][0]

            text_boxes.add(svg_shapes.Rect(
                insert=(x_text_left - 40 + (text_box_width + 20) * label_offset, y_p - 40 + pin * 100),
                size=(text_box_width, 80),
                rx=40, ry=40, stroke=stroke_color, fill=color, stroke_width=5
            ))

            text.add(svg_text.Text(
                str(functions.attrib['label']),
                insert=(x_text_left + text_box_width/2 - 40 + (text_box_width + 20)*label_offset, y_p + 20 + pin * 100),
                stroke='none', fill=text_color, font_family=FONTS['label'], font_size=60, text_anchor="middle"
            ))
            
            label_offset -= 1

    # Reset the zigzag polarity
    if zigzag < 0:
        zigzag *= -1

    # Right/second row, reversed iteration
    for pin in reversed(range(number_of_rows, number_of_pins)):
        color = get_label_color(pin_out[pin][0].attrib['category'])

        # Lines to labels
        if pin_out[pin][0].attrib['label'] != "":
            text_boxes.add(
                svg_shapes.Rect(
                    insert=(board_origin_x + width - 5,
                            y_p - 5 + ((number_of_rows - 1) * 100) - (pin - number_of_rows) * 100),
                    size=(x_text_right - (board_origin_x + width) + 10, 10),
                    rx=5, ry=5, stroke=color, fill=color
                )
            )
        label_offset = 0
        for functions in pin_out[pin]:
            color = get_label_color(functions.attrib['category'])

            if label_offset == 0:
                # Check if the pin is NC
                cnano_pin_label = ""
                if str(functions.attrib['label']) == "":
                    cnano_pin_label = "NC"
                else:
                    cnano_pin_label = str(functions.attrib['label'])

                text.add(svg_text.Text(
                    cnano_pin_label,
                    insert=(board_origin_x + width + (zigzag*1.5) - 150 - 10,
                            y_p + ((number_of_rows - 1) * 100) - (pin - number_of_rows) * 100),
                    stroke="none", fill="white", font_family=FONTS['pin'], font_size=30,
                    glyph_orientation_vertical=90, writing_mode="tb", text_anchor="middle"
                ))
                zigzag *= -1

                # If the pin is NC this functions should break
                if str(functions.attrib['label']) == "":
                    break

            if get_lightness(color) > TEXTBOX_LIGHTNESS_THRESHOLD:  # Should use black text?
                text_color = '#000000'
            else:
                text_color = '#FFFFFF'

            stroke_color = color
            if functions.attrib['category'] in ["PORT", "MVIO"]:
                if len(ROOT.findall(".//*[@label='{}']".format(functions.attrib['label']))) > 1:
                    if functions.attrib['label'] != 'NC':
                        stroke_color = PIN_TYPES['SHARED'][0]

            text_boxes.add(svg_shapes.Rect(
                insert=(x_text_right - 40 + (text_box_width + 20) * label_offset,
                        y_p - 40 + ((number_of_rows - 1) * 100) - (pin - number_of_rows) * 100),
                size=(text_box_width, 80),
                rx=40, ry=40, stroke=stroke_color, fill=color, stroke_width=5
            ))

            text.add(svg_text.Text(
                str(functions.attrib['label']),
                insert=(x_text_right + text_box_width/2 - 40 + (text_box_width + 20)*label_offset,
                        y_p + 20 + ((number_of_rows - 1) * 100) - (pin - number_of_rows) * 100),
                stroke='none', fill=text_color, font_family=FONTS['label'], font_size=60, text_anchor="middle"
            ))

            label_offset += 1

    text.add(svg_text.Text(
        str("DEBUGGER"),
        insert=(board_origin_x + width/2, board_origin_y + 830),
        stroke='none', fill="white", font_family=FONTS['kit_name'], font_size=60, text_anchor="middle"
    ))

    text.add(svg_shapes.Rect(
        insert=(board_origin_x - 10, board_origin_y + 845),
        size=(width + 20, 10),
        rx=5, ry=5, stroke='none', fill='white'
    ))

    text.add(svg_text.Text(
        str(pin_out.attrib["device"]),
        insert=(board_origin_x + width/2, board_origin_y + 915),
        stroke='none', fill="white", font_family=FONTS['kit_name'], font_size=60, text_anchor="middle"
    ))


    # Title
    title = dwg.add(dwg.g(id='title', stroke_width='2'))

    title.add(svg_text.Text(
        str(pin_out.attrib["device"]),
        insert=(board_origin_x - 500, board_origin_y - 200), font_family=FONTS['kit_name'],
        font_size=200, text_anchor="middle"))

    title.add(svg_text.Text(
        str("Curiosity Nano"),
        insert=(board_origin_x - 500, board_origin_y - 50), font_family=FONTS['kit_name'],
        font_size=125, text_anchor="middle"))

    view_box_x = width + ((text_box_width + 20) * max_labels + 169)*2 + 20
    view_box_y = length + board_origin_y
    scale = (px_pr_cm * svg_width)/view_box_x

    ret_dwg = dwg.copy()

    dwg.viewbox(100, 100, view_box_x, view_box_y)
    dwg['height'] = ((view_box_y * scale) / px_pr_cm)*cm
    dwg['width'] = ((view_box_x * scale) / px_pr_cm)*cm
    dwg.fit('center', 'middle', 'meet')
    try:
        dwg.save(pretty=True)
    except IOError:
        print("Unable to save to file: {}".format(name))

    return ret_dwg, view_box_x, view_box_y


def mbus(name, pin_out, cnano_svg, cnano_width, cnano_height):
    """
    Convert the pin out to SVG

    Outline for MBUS:
          _________
    AN   |  MBUS   | PWM
    RST  |         | INT
    CS   |         | RX
    SCK  |         | TX
    MISO |         | SCL
    MOSI |         | SDA
    3.3V |         | 5V
    GND  |_________| GND
                  /

    :param name: File name of the output SVG
    :param pin_out: XML input for parsing
    :param cnano_svg: SVG of the CNANO board
    :param cnano_width: width of the SVG
    :param cnano_height: height of the SVG
    """
    number_of_pins = len(pin_out)

    if number_of_pins % 2:
        raise ValueError("Odd number of pins defined")

    number_of_rows = int(number_of_pins / 2)
    svg_width = 15  # in cm
    px_pr_cm = 37.795

    # Size of the mbus outline
    length = 1125
    width = 1100
    space_x = 2000
    space_y = 1500

    text_origin_x = cnano_width + 200
    hole_r = 25  # hole radius
    text_box_width = 262

    # dwg = Drawing(filename=name, size=(svg_width, svg_width))
    dwg = cnano_svg

    # Create layers for the drawing, first layer = bottom layer
    outline = dwg.add(dwg.g(id='mbus_outline', stroke=COLORS['outline'][0],
                            fill='none', stroke_width=COLORS['outline'][2]))
    mbus_logo = dwg.add(dwg.g(id='mbus_logo', stroke='none', fill='black', stroke_width=0.2))
    holes = dwg.add(dwg.g(id='mbus_holes', stroke=COLORS['holes'][0], fill=COLORS['holes'][1],
                          stroke_width=COLORS['holes'][2]))
    # origin = dwg.add(dwg.g(id='origin'))
    text_boxes = dwg.add(dwg.g(id='mbus_text_boxes', stroke_width='2'))
    text = dwg.add(dwg.g(id='mbus_text', stroke='none', fill="black", font_family=FONTS['pin'], font_size=60,
                         text_anchor="middle"))

    # Upper left corner of the board, x-coordinate must be computed first
    board_origin_x = text_origin_x + (text_box_width + 20)
    board_origin_y = 475

    coords = [(board_origin_x, board_origin_y + 200),
              (board_origin_x, board_origin_y + space_y + 200),
              (board_origin_x + space_x, board_origin_y + 200),
              (board_origin_x + space_x, board_origin_y + space_y + 200)]

    # Draw the board logo, outline frame and pin function:
    logo_width = 467
    logo_path = svg_path.Path()
    mbus_path = svg_path.Path('M{} {} {}'.format(coords[3][0], coords[3][1], XPRO_OUTLINE))

    # Add pin holes for mbus
    for run, (coord_x, coord_y) in enumerate(coords[:3], start=1):
        logo_path.push('M{} {} {}'.format(coord_x + width / 2 - logo_width / 2, coord_y, MBUS))
        mbus_path.push('M{} {} {}'.format(coord_x, coord_y, MBUS_OUTLINE))
        text.add(svg_text.Text(str(run), insert=(coord_x + 550, coord_y + 950), font_size=200))
        holes.add(dwg.rect((coord_x + 100 - hole_r, coord_y + 225 - hole_r), (hole_r * 2, hole_r * 2)))
        holes.add(dwg.rect((coord_x + 1000 - hole_r, coord_y + 225 - hole_r), (hole_r * 2, hole_r * 2)))
        for row in range(8):
            holes.add(dwg.circle(center=(coord_x + 100, coord_y + 225 + row * 100), r=hole_r))
            holes.add(dwg.circle(center=(coord_x + 1000, coord_y + 225 + row * 100), r=hole_r))
            text.add(svg_text.Text(str(LABELS_LEFT[row]), insert=(coord_x + 175, coord_y + 250 + 100 * row),
                                   text_anchor="start"))
            text.add(svg_text.Text(str(LABELS_RIGHT[row]), insert=(coord_x + 925, coord_y + 250 + 100 * row),
                                   text_anchor="end"))

    outline.add(mbus_path)
    mbus_logo.add(logo_path)

    # Add outline for XPRO
    text.add(svg_text.Text(str("Xplained Pro Extension"),
                           insert=(coords[3][0] + width / 2, coords[3][1] - 100), font_size=100))
    text.add(svg_text.Text(str("EXT1"), insert=(coords[3][0] + width / 2, coords[3][1]), font_size=50))
    text.add(svg_text.Text(str("1"), insert=(coords[3][0] + width / 2 - 50, coords[3][1] + 50), font_size=50))
    text.add(svg_text.Text(str("2"), insert=(coords[3][0] + width / 2 + 50, coords[3][1] + 50), font_size=50))
    text.add(svg_text.Text(str("19"), insert=(coords[3][0] + width / 2 - 50, coords[3][1] + 1150), font_size=50))
    text.add(svg_text.Text(str("20"), insert=(coords[3][0] + width / 2 + 50, coords[3][1] + 1150), font_size=50))
    holes.add(dwg.rect((coords[3][0] + width / 2 - 50 - hole_r, coords[3][1] + 125 - hole_r), (hole_r * 2, hole_r * 2)))
    for row in range(10):
        holes.add(dwg.circle(center=(coords[3][0] + width / 2 - 50, coords[3][1] + 125 + row * 100), r=hole_r))
        holes.add(dwg.circle(center=(coords[3][0] + width / 2 + 50, coords[3][1] + 125 + row * 100), r=hole_r))

    text.add(svg_text.Text(str("Curiosity Nano Base"),
                           insert=(board_origin_x + (space_x - width) / 2 + width, board_origin_y), font_size=200))
    text.add(svg_text.Text(str("for Click boards"),
                           insert=(board_origin_x + (space_x - width) / 2 + width, board_origin_y+150), font_size=125))
    text.add(svg_text.Text(str("TM"),
                           insert=(board_origin_x + (space_x - width) / 2 + width + 525, board_origin_y + 110),
                           font_size=70))

    # Mapping of the CNANO to the Adapter MBUS pinout
    mbus_conn = [[(-14, -11), (-7, -8), (13, 7), (12, 6), (11, 9), (10, 8), (-6, -1), (-5, -5)],
                 [(-13, -10), (18, 17), (-17, 16), (12, 15), (11, 9), (10, 8), (-6, -1), (-5, -5)],
                 [(-12, -9), (-18, -19), (-16, 7), (12, 6), (11, 9), (10, 8), (-6, -1), (-5, -5)]]

    mbus_conn_color = [["ANALOG", "PORT", "SPI", "SPI", "SPI", "SPI", "POWER", "GND"],
                       ["TIMER", "PORT", "UART", "UART", "I2C", "I2C", "POWER", "GND"]]

    # Add pin out labels
    # Left/first row
    for run, conn in enumerate(mbus_conn):

        # Coordinates for on-board things
        x_text_left = coords[run][0] - 100 - (text_box_width - 80)  # x-coordinate for label text on left side
        x_text_right = coords[run][0] + width + 100  # y-coordinate for origin of first label text on right side
        row_p = coords[run][1] + 225  # y-coordinate for upper pin hole

        for offset, (pin_left, pin_right) in enumerate(conn):
            # If pin is available, don't wrap around
            pin_left_text = pin_out[pin_left][0].attrib['label']
            if pin_left_text != "":
                if -number_of_rows <= pin_left < number_of_rows:
                    if pin_left == -6:
                        pin_left_text = "+3.3V"

                    color1 = PIN_TYPES[mbus_conn_color[0][offset]][1]

                    # Lines to labels
                    text_boxes.add(svg_shapes.Rect(insert=(coords[run][0] - 100, row_p - 5 + offset * 100),
                                                size=(150, 10), rx=5, ry=5, stroke=color1, fill=color1))
                    text_color1 = '#FFFFFF'
                    if get_lightness(color1) > TEXTBOX_LIGHTNESS_THRESHOLD:  # Should use black text?
                        text_color1 = '#000000'

                    # Box around text
                    text_boxes.add(svg_shapes.Rect(insert=(x_text_left - 40, row_p - 40 + offset * 100),
                                                size=(text_box_width, 80), rx=40, ry=40,
                                                stroke=color1, fill=color1, stroke_width=5))
                    text.add(svg_text.Text(str(pin_left_text),
                                        insert=(x_text_left + text_box_width / 2 - 40, row_p + 20 + offset * 100),
                                        stroke='none', fill=text_color1, font_family=FONTS['label'], font_size=60,
                                        text_anchor="middle"))

            # If pin is available, don't wrap around
            pin_right_text = pin_out[pin_right][0].attrib['label']
            if pin_right_text != "":
                if -number_of_rows <= pin_right < number_of_rows:   
                    if pin_right == -1:
                        pin_right_text = "+5V"

                    color2 = PIN_TYPES[mbus_conn_color[1][offset]][1]
                    # Lines to labels
                    text_boxes.add(svg_shapes.Rect(insert=(coords[run][0] + width - 50, row_p - 5 + offset * 100),
                                                size=(150, 10), rx=5, ry=5, stroke=color2, fill=color2))
                    text_color2 = '#FFFFFF'
                    if get_lightness(color2) > TEXTBOX_LIGHTNESS_THRESHOLD:  # Should use black text?
                        text_color2 = '#000000'

                    # Box around text
                    text_boxes.add(svg_shapes.Rect(insert=(x_text_right - 40, row_p - 40 + offset * 100),
                                                size=(text_box_width, 80), rx=40, ry=40,
                                                stroke=color2, fill=color2, stroke_width=5))

                    text.add(svg_text.Text(str(pin_right_text),
                                        insert=(x_text_right + text_box_width / 2 - 40, row_p + 20 + offset * 100),
                                        stroke='none', fill=text_color2, font_family=FONTS['label'], font_size=60,
                                        text_anchor="middle"))

    # Mapping of the CNANO to the Adapter XPRO extension pinout
    xpro_conn = [(1, -5), (-13, -12), (18, -18), (-10, -9), (17, -16), (8, 9), (16, 15), (-17, 10), (11, 12), (-5, -6)]
    xpro_conn_color = [["DEBUG", "ANALOG", "PORT", "TIMER", "PORT", "I2C", "UART", "SPI", "SPI", "GND"],
                       ["GND", "ANALOG", "PORT", "TIMER", "SPI", "I2C", "UART", "SPI", "SPI", "POWER"]]

    # Coordinates for on-board things
    x_text_left = coords[3][0] + 350 - (text_box_width - 80)  # x-coordinate for label text on left side
    x_text_right = coords[3][0] + 750  # y-coordinate for origin of first label text on right side
    row_p = coords[3][1] + 125  # y-coordinate for upper pin hole

    for offset, (pin_left, pin_right) in enumerate(xpro_conn):

        # Text
        pin_left_text = pin_out[pin_left][0].attrib['label']
        if pin_left_text != "":
            if -number_of_rows <= pin_left < number_of_rows:
                color1 = PIN_TYPES[xpro_conn_color[0][offset]][1]
                # Lines to labels
                text_boxes.add(svg_shapes.Rect(insert=(coords[3][0] + 300, row_p - 5 + offset * 100),
                                            size=(150, 10), rx=5, ry=5, stroke=color1, fill=color1))
                text_color1 = '#FFFFFF'
                if get_lightness(color1) > TEXTBOX_LIGHTNESS_THRESHOLD:  # Should use black text?
                    text_color1 = '#000000'
                # Box around text
                text_boxes.add(svg_shapes.Rect(insert=(x_text_left - 40, row_p - 40 + offset * 100),
                                            size=(text_box_width, 80), rx=40, ry=40,
                                            stroke=color1, fill=color1, stroke_width=5))

                text.add(svg_text.Text(str(pin_left_text),
                                    insert=(x_text_left + text_box_width / 2 - 40, row_p + 20 + offset * 100),
                                    stroke='none', fill=text_color1, font_family=FONTS['label'], font_size=60,
                                    text_anchor="middle"))

        pin_right_text = pin_out[pin_right][0].attrib['label']
        if pin_right_text != "":
            if -number_of_rows <= pin_right < number_of_rows:
                if pin_right == -6:
                    pin_right_text = "+3.3V"

                color2 = PIN_TYPES[xpro_conn_color[1][offset]][1]
                # Lines to labels
                text_boxes.add(svg_shapes.Rect(insert=(coords[3][0] + 700 - 50, row_p - 5 + offset * 100),
                                            size=(150, 10), rx=5, ry=5, stroke=color2, fill=color2))
                text_color2 = '#FFFFFF'
                if get_lightness(color2) > TEXTBOX_LIGHTNESS_THRESHOLD:  # Should use black text?
                    text_color2 = '#000000'

                # Box around text
                text_boxes.add(svg_shapes.Rect(insert=(x_text_right - 40, row_p - 40 + offset * 100),
                                            size=(text_box_width, 80), rx=40, ry=40,
                                            stroke=color2, fill=color2, stroke_width=5))

                text.add(svg_text.Text(str(pin_right_text),
                                    insert=(x_text_right + text_box_width / 2 - 40, row_p + 20 + offset * 100),
                                    stroke='none', fill=text_color2, font_family=FONTS['label'], font_size=60,
                                    text_anchor="middle"))

    view_box_x = board_origin_x + width + space_x + text_box_width
    view_box_y = max(board_origin_y + length + space_y + 200, cnano_height)
    scale = (px_pr_cm * svg_width)/view_box_y

    for obj in dwg.elements:
        obj.matrix(0, -1, 1, 0, 0, view_box_x + 200)

    dwg.viewbox(100, 100, view_box_y, view_box_x)
    dwg['height'] = ((view_box_x * scale) / px_pr_cm)*cm
    dwg['width'] = ((view_box_y * scale) / px_pr_cm)*cm
    dwg.fit('center', 'middle', 'meet')
    try:
        dwg.saveas(name, pretty=True)
    except IOError:
        print("Unable to save to file: {}".format(name))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("Input file: {}".format(sys.argv[1]))
        INPUT_FILE = sys.argv[1]
    else:
        print("Usage: {} INPUT_FILE.NET or INPUT_FILE.XML".format(sys.argv[0]))
        sys.exit("No input file given.")

    FILE_NAME, FILE_EXT = INPUT_FILE.rsplit(".", 1)
    OUTPUT_FILE = "{}.svg".format(FILE_NAME)
    MBUS_OUTPUT_FILE = "{}_MBUS.svg".format(FILE_NAME)
    PIN_OUT_TREE = ""

    if FILE_EXT.lower() == "net":
        try:
            print("Parsing file: {}".format(sys.argv[1]))
            XML_STR = netlist_to_pin_out(INPUT_FILE)
            XML_FILE = "{}.xml".format(FILE_NAME)
            # Save xml to file
            with open(XML_FILE, "wb") as fh:
                fh.write(XML_STR)
            PIN_OUT_TREE = ETree.parse(XML_FILE)
        except IOError as error:
            print("Something went wrong parsing Net list:\n{}".format(error))
            sys.exit(0)
    elif FILE_EXT.lower() == "xml":
        PIN_OUT_TREE = ETree.parse(INPUT_FILE)
    else:
        print("Not valid input file extension: {}".format(FILE_EXT))
        sys.exit(0)

    ROOT = PIN_OUT_TREE.getroot()

    if "device" in ROOT.attrib:
        print("Device name: {}".format(ROOT.attrib["device"]))
    else:
        print("Missing device info.. Add device=\'your device\' in XML")
        sys.exit(0)

    print("Saving file as: {}".format(OUTPUT_FILE))
    SVG_CNANO, SVG_X, SVG_Y = cnano(OUTPUT_FILE, ROOT)
    print("Saving file as: {}".format(MBUS_OUTPUT_FILE))
    mbus(MBUS_OUTPUT_FILE, ROOT, SVG_CNANO, SVG_X, SVG_Y)
