# Event - Read_event_settings, Route_logic_pins, Simple_event

### Example Code
```
/***********************************************************************|
| megaAVR event system library                                          |
|                                                                       |
| Read_event_settings.ino                                               |
|                                                                       |
| A library for interfacing with the megaAVR event system.              |
| Developed in 2021 by MCUdude                                          |
| https://github.com/MCUdude/                                           |
|                                                                       |
| In this example, we demonstrate the possibilities of reading out what |
| event channel we're working with, what generator is used, and which   |
| channel an event user has been connected to.                          |
|                                                                       |
| See Microchip's application note AN2451 for more information.         |
|***********************************************************************/

#include <Event.h>

// Function to print information about the passed event
void print_event_info(Event &my_event) {
  Serial2.printf("This is event channel no. %d\n", my_event.get_channel_number());
  Serial2.printf("This channel uses generator no. 0x%02x, which you can find in Event.h\n", my_event.get_generator());
}

void print_user_info(user::user_t my_user) {
  // Event::get_user_channel() returns -1 if the user isn't connected to any event generator
  Serial2.printf("User 0x%02x is connected to event channel no. %d\n\n", my_user, Event::get_user_channel(my_user));
}

void setup() {
  Serial2.begin(9600); // Initialize hardware serial port

  Event4.set_generator(gen4::pin_pe0); // Set pin PE0 as event generator
  Event5.set_generator(gen5::pin_pe1); // Set pin PE1 as event generator

  // For more information about EVOUT, see the PORTMUX section in the datasheet
  Event4.set_user(user::evoute_pin_pe2); // Set EVOUTE as event user
  Event5.set_user(user::evoutf_pin_pf2); // Set EVOUTF as event user

  // Start event channels
  Event4.start();
  Event5.start();
}

void loop() {
  // Print info about Event4 and its event user
  print_event_info(Event4);
  print_user_info(user::evoute_pin_pe2);

  // Print info about Event5 and its event user
  print_event_info(Event5);
  print_user_info(user::evoutf_pin_pf2);

  delay(5000);
}
```
```
/***********************************************************************|
| megaAVR event system library                                          |
|                                                                       |
| Read_event_settings.ino                                               |
|                                                                       |
| A library for interfacing with the megaAVR event system.              |
| Developed in 2021 by MCUdude                                          |
| https://github.com/MCUdude/                                           |
|                                                                       |
| In this example, we demonstrate the possibilities of reading out what |
| event channel we're working with, what generator is used, and which   |
| channel an event user has been connected to.                          |
|                                                                       |
| See Microchip's application note AN2451 for more information.         |
|***********************************************************************/

#include <Event.h>

// Function to print information about the passed event
void print_event_info(Event &my_event) {
  Serial2.printf("This is event channel no. %d\n", my_event.get_channel_number());
  Serial2.printf("This channel uses generator no. 0x%02x, which you can find in Event.h\n", my_event.get_generator());
}

void print_user_info(user::user_t my_user) {
  // Event::get_user_channel() returns -1 if the user isn't connected to any event generator
  Serial2.printf("User 0x%02x is connected to event channel no. %d\n\n", my_user, Event::get_user_channel(my_user));
}

void setup() {
  Serial2.begin(9600); // Initialize hardware serial port

  Event4.set_generator(gen4::pin_pe0); // Set pin PE0 as event generator
  Event5.set_generator(gen5::pin_pe1); // Set pin PE1 as event generator

  // For more information about EVOUT, see the PORTMUX section in the datasheet
  Event4.set_user(user::evoute_pin_pe2); // Set EVOUTE as event user
  Event5.set_user(user::evoutf_pin_pf2); // Set EVOUTF as event user

  // Start event channels
  Event4.start();
  Event5.start();
}

void loop() {
  // Print info about Event4 and its event user
  print_event_info(Event4);
  print_user_info(user::evoute_pin_pe2);

  // Print info about Event5 and its event user
  print_event_info(Event5);
  print_user_info(user::evoutf_pin_pf2);

  delay(5000);
}


```
```
/***********************************************************************|
| megaAVR event system library                                          |
|                                                                       |
| Simple_Event.ino                                                      |
|                                                                       |
| A library for interfacing with the megaAVR event system.              |
| Developed in 2021 by MCUdude                                          |
| https://github.com/MCUdude/                                           |
|                                                                       |
| In this example we use pin PE0 as an event generator, and pin PE2 and |
| PF2 as event users. In practive, pin PE2 and PF2 will follow          |
| PE0's state.                                                          |
|                                                                       |
| See Microchip's application note AN2451 for more information.         |
|***********************************************************************/

#include <Event.h>

void setup() {
  // Since pin PE0 is only available on event generator channel 4 and 5, we use Event4 as our object
  // Note that we use gen4:: to refer to functionality unique to event channel 4
  Event4.set_generator(gen4::pin_pe0); // Set pin PE0 as event generator

  // For more information about EVOUT, see the PORTMUX section in the datasheet
  Event4.set_user(user::evoute_pin_pe2); // Set EVOUTE as event user
  Event4.set_user(user::evoutf_pin_pf2); // Set EVOUTF as event user

  // Start the event channel
  Event4.start();
}

void loop() {

}
```


### Result
Error compiling for board AVR DA-series.


### Messages
```

In file included from C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\examples\Read_event_settings\Read_event_settings.ino:17:0:
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen0::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:654:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator, 0); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen1::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:657:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator, 1); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen2::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:660:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator, 2); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen3::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:663:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator, 3); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen4::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:666:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator, 4); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen5::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:669:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator, 5); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen6::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:672:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator, 6); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen7::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:675:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator, 7); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen8::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:678:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator, 8); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen9::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:681:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator, 9); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
exit status 1
Error compiling for board AVR DA-series.



```
```
In file included from C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\examples\Route_logic_pins\Route_logic_pins.ino:32:0:
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen0::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:654:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator, 0); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen1::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:657:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator, 1); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen2::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:660:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator, 2); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen3::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:663:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator, 3); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen4::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:666:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator, 4); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen5::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:669:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator, 5); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen6::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:672:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator, 6); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen7::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:675:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator, 7); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen8::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:678:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator, 8); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen9::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:681:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator, 9); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
exit status 1
Error compiling for board AVR DA-series.



```
```
In file included from C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\examples\Simple_event\Simple_event.ino:17:0:
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen0::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:654:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator, 0); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen1::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:657:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator, 1); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen2::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:660:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator, 2); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen3::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:663:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator, 3); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen4::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:666:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator, 4); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen5::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:669:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator, 5); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen6::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:672:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator, 6); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen7::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:675:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator, 7); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen8::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:678:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator, 8); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h: In static member function 'static Event& Event::assign_generator(gen9::generator_t)':
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:681:113: error: no matching function for call to 'Event::set_generator(gen::generator_t, int)'
       static Event& assign_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator, 9); }
                                                                                                                 ^
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note: candidate: void Event::set_generator(gen::generator_t)
     void set_generator(gen::generator_t generator);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:614:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note: candidate: void Event::set_generator(uint8_t)
     void set_generator(uint8_t pin_number);
          ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:615:10: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note: candidate: void Event::set_generator(gen0::generator_t)
       void set_generator(gen0::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:618:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note: candidate: void Event::set_generator(gen1::generator_t)
       void set_generator(gen1::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:621:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note: candidate: void Event::set_generator(gen2::generator_t)
       void set_generator(gen2::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:624:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note: candidate: void Event::set_generator(gen3::generator_t)
       void set_generator(gen3::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:627:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note: candidate: void Event::set_generator(gen4::generator_t)
       void set_generator(gen4::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:630:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note: candidate: void Event::set_generator(gen5::generator_t)
       void set_generator(gen5::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:633:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note: candidate: void Event::set_generator(gen6::generator_t)
       void set_generator(gen6::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:636:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note: candidate: void Event::set_generator(gen7::generator_t)
       void set_generator(gen7::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:639:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note: candidate: void Event::set_generator(gen8::generator_t)
       void set_generator(gen8::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:642:12: note:   candidate expects 1 argument, 2 provided
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note: candidate: void Event::set_generator(gen9::generator_t)
       void set_generator(gen9::generator_t generator) { set_generator((gen::generator_t)generator); }
            ^~~~~~~~~~~~~
C:\Users\ivanFernandez\AppData\Local\Arduino15\packages\Microchip\hardware\megaavr\1.0.0\libraries\Event\src/Event.h:645:12: note:   candidate expects 1 argument, 2 provided
exit status 1
Error compiling for board AVR DA-series.
```
### Notes
1.  The Sketch Read_event_settings does not compile successfully.  Compile error messages point to the Event.h file which is included in the Sketch.  
There seems to be an incompatibility with the AVR-DA series board and the method calls to void Event::set_generator().   note:   candidate expects 1 argument, 2 provided.

2.  The Sketch Read_logic_pins does not compile successfully.  Compile error messages point to the Event.h file which is included in the Sketch.  
There seems to be an incompatibility with the AVR-DA series board and the method calls to void Event::set_generator().   note:   candidate expects 1 argument, 2 provided.


3.  The Sketch Simple_event does not compile successfully.  Compile error messages point to the Event.h file which is included in the Sketch.  
There seems to be an incompatibility with the AVR-DA series board and the method calls to void Event::set_generator().   note:   candidate expects 1 argument, 2 provided.


