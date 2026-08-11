# Practical 3_2 — GPIO LED Output

## Aim
To control a standard Light Emitting Diode (LED) using the Raspberry Pi's GPIO pins.

## Learning Objectives
* Learn how to configure a GPIO pin as an output.
* Understand the concept of a main loop with a `sleep` interval.
* Practice safe GPIO cleanup on program exit.

## Components Required
* Raspberry Pi
* 1x LED (any color)
* 1x 220-330Ω Resistor
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* LED Anode (long leg) -> 330Ω Resistor -> GPIO 17 (BCM)
* LED Cathode (short leg) -> GND

## Software Requirements
* `nielit_rpi` library

## How It Works
The program initializes an `LEDController` object targeting GPIO 17. In an infinite `while` loop, it toggles the state of the LED using the `on()` and `off()` methods, pausing for one second between state changes using `time.sleep()`.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
Blinking LED on GPIO 17. Press Ctrl+C to stop.
```
(The physical LED will blink repeatedly).

## Troubleshooting
* **LED not lighting up**: Check the polarity of the LED (Anode to GPIO, Cathode to GND).
* **LED very dim or bright**: Check the resistor value. A 220-330Ω resistor is recommended.
* **Permission denied**: Ensure your user is part of the `gpio` group.

## Safety Notes
* **Always use a current-limiting resistor** when connecting an LED to prevent damage to the GPIO pin.

## GPIO Reference
* All practicals use BCM numbering.
