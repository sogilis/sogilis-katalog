# LED DRIVER

Extract from the book ***Test-Driven Development for Embedded C*** by James W. Grenning.
https://github.com/jwgrenning/tddec-code

## Requirements
- The led driver controls 16 two-states leds.
- The driver can turn on or off individual led without affecting others.
- The driver can turn all leds on or off with a single interface call.
- The user of the driver can query the state of any led.
- At power-on, the hardware default is for leds to be latched on. They must be turned off by the software.
- The leds are memory-mapped to a 16 bit word (at an address to be determined).
- A 1 in a bit position lights the corresponding led, a 0 turns it off.
- The least significant bit corresponds to the Led1.
- The most significant bit corresponds to the Led16.

## Archi Design
- Single-instance design model.
- Must be testable off the target hardware.
- I/O mapped address is write-only.

## Improvements
- Monitoring runtime error.
- Board used an inverted logic.
- Supported both logic (inverted and not), don’t use conditional compilation !
- Problem on hardware : LED1 is labeled 16, LED2 is 15 …

## Tips for a test list
- All leds are off after the driver is initialized.
- A single led can be turned on.
- A single led can be turned off.
- Multiple leds can be turned on or off.
- Turn on all leds.
- Turn off all leds.
- Query led state.
- Check boundary values.
- Check out-of-bounds values.
