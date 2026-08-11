# Practical 3_3 — Push Button Input

## Aim
To read digital input from a momentary push button using the Raspberry Pi.

## Learning Objectives
* Learn how to configure a GPIO pin as an input.
* Understand the concept of internal pull-up resistors.
* Practice reading and displaying real-time sensor data.

## Components Required
* Raspberry Pi
* 1x Momentary Push Button
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* Button Pin 1 -> GPIO 27 (BCM)
* Button Pin 2 -> GND

## Software Requirements
* `nielit_rpi` library

## How It Works
The program initializes a `ButtonReader` on GPIO 27 with the internal pull-up resistor enabled. This means the pin defaults to HIGH when unpressed. When the button is pressed, the circuit connects to GND, pulling the pin LOW. The script polls this state every 0.1 seconds and prints the result.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
Monitoring Button on GPIO 27. Press Ctrl+C to stop.
Button State: RELEASED
```
(When pressed, the text changes to `PRESSED`).

## Troubleshooting
* **Button state always PRESSED**: Check your wiring; the button may be shorted to GND permanently.
* **Button state always RELEASED**: Ensure the button is properly inserted into the breadboard (straddling the gap).
* **Multiple triggers**: This script relies on polling; bouncing is usually handled internally by the library, but if an issue arises, check wiring integrity.

## Safety Notes
* Double-check connections before powering the Pi to avoid shorts.

## GPIO Reference
* All practicals use BCM numbering.
