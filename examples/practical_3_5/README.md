# Practical 3_5 — Traffic Light Controller

## Aim
To simulate a traffic light sequence using multiple LEDs.

## Learning Objectives
* Learn how to manage multiple output pins simultaneously.
* Understand sequential timing and logic flow.
* Reinforce safe initialization and cleanup practices.

## Components Required
* Raspberry Pi
* 1x Red LED, 1x Yellow LED, 1x Green LED
* 3x 220-330Ω Resistors
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* Red LED Anode -> Resistor -> GPIO 17
* Yellow LED Anode -> Resistor -> GPIO 27
* Green LED Anode -> Resistor -> GPIO 22
* All LED Cathodes -> GND

## Software Requirements
* `nielit_rpi` library

## How It Works
The script initializes three `LEDController` instances. It enters an infinite loop, executing a standard traffic light sequence: Red (5 seconds), Green (5 seconds), and Yellow (2 seconds). It ensures that all LEDs are turned off when the program is interrupted.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
Starting Traffic Light Controller. Press Ctrl+C to stop.
```

## Troubleshooting
* **Wrong sequence order**: Check your wiring and ensure the physical LEDs match the GPIO pins defined in the script.
* **Multiple LEDs on at once**: The script turns off the active LED before turning on the next; if multiple are on, check for crossed wires on the breadboard.
* **LEDs not lighting**: Check polarity and verify the resistors are placed correctly.

## Safety Notes
* Use a separate current-limiting resistor for each LED. Do not share one resistor across multiple LEDs.

## GPIO Reference
* All practicals use BCM numbering.
