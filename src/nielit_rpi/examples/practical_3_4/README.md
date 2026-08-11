# Practical 3_4 — Button Controlled LED

## Aim
To create an interactive circuit where a push button directly controls the state of an LED.

## Learning Objectives
* Learn how to combine multiple GPIO components (input and output).
* Understand how to map input states to output actions.
* Practice writing reactive code.

## Components Required
* Raspberry Pi
* 1x LED (any color)
* 1x 220-330Ω Resistor
* 1x Momentary Push Button
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* LED Anode -> 330Ω Resistor -> GPIO 17
* LED Cathode -> GND
* Button Pin 1 -> GPIO 27
* Button Pin 2 -> GND

## Software Requirements
* `nielit_rpi` library

## How It Works
The script initializes both an `LEDController` and a `ButtonReader`. It polls the button's state in a continuous loop; if the button reads as pressed, it commands the LED to turn on. Otherwise, it commands the LED to turn off.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
Control LED (GPIO 17) with Button (GPIO 27).
Press Ctrl+C to stop.
```

## Troubleshooting
* **LED doesn't light up**: Check LED polarity and resistor.
* **LED is always on**: The button might be wired incorrectly (shorted to ground permanently).
* **Flickering LED**: Ensure the jumper wires are securely seated in the breadboard.

## Safety Notes
* Ensure the LED has a current-limiting resistor.

## GPIO Reference
* All practicals use BCM numbering.
