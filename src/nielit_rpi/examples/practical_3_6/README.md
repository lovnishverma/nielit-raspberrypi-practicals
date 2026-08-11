# Practical 3_6 — PWM LED Brightness

## Aim
To control the brightness of an LED using Pulse Width Modulation (PWM).

## Learning Objectives
* Understand the concept of PWM and its use cases.
* Learn how to vary duty cycle to control perceived brightness.
* Work with hardware-capable PWM pins on the Raspberry Pi.

## Components Required
* Raspberry Pi
* 1x LED
* 1x 220-330Ω Resistor
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* LED Anode -> Resistor -> GPIO 18 (PWM0)
* LED Cathode -> GND

## Software Requirements
* `nielit_rpi` library

## How It Works
The script utilizes the `PWMLEDController` to manage GPIO 18, which supports hardware PWM. By rapidly toggling the power on and off (the duty cycle), the LED's perceived brightness changes. The script loops, incrementally increasing the duty cycle from 0 to 1 and then decreasing it back to 0.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
Fading LED on GPIO 18 using PWM. Running 3 cycles.
Cycle 1/3
Cycle 2/3
Cycle 3/3
```

## Troubleshooting
* **LED turns on and off instantly without fading**: Ensure you are connected to GPIO 18, as some pins do not support hardware PWM effectively.
* **Flickering effect instead of smooth fade**: Check background processes on the Raspberry Pi; high CPU load can sometimes interrupt software PWM timing if hardware PWM isn't properly engaged.

## Safety Notes
* Use a current-limiting resistor to protect the GPIO pin.

## GPIO Reference
* All practicals use BCM numbering.
