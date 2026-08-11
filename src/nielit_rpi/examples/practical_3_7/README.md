# Practical 3_7 — Buzzer Alert

## Aim
To generate audible alerts using an active buzzer module.

## Learning Objectives
* Interface an active buzzer with the Raspberry Pi.
* Understand the difference between active and passive buzzers.
* Control the timing of output signals to create sound patterns.

## Components Required
* Raspberry Pi
* 1x Active Buzzer Module
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* Buzzer VCC / '+' -> GPIO 23
* Buzzer GND / '-' -> GND

*(Note: Some modules may require connecting VCC to 3.3V, GND to GND, and an 'I/O' pin to the GPIO).*

## Software Requirements
* `nielit_rpi` library

## How It Works
An active buzzer contains a built-in oscillator; supplying a DC voltage causes it to emit a tone. The `BuzzerController` treats the buzzer similarly to an LED. The script toggles the pin high for 0.2 seconds and low for 0.2 seconds in a loop to create a beeping effect.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
Sounding buzzer on GPIO 23 for 5 beeps.
```

## Troubleshooting
* **No sound**: Ensure the buzzer is correctly oriented (check the '+' marking). Verify it is an *active* buzzer, not a passive one.
* **Low volume**: Check the voltage requirements of your buzzer. If it requires 5V, do not drive it directly from the 3.3V GPIO pin without a transistor circuit.
* **Continuous sound**: Ensure your script is shutting the buzzer off correctly in the `finally` block.

## Safety Notes
* Do not drive high-current 5V buzzers directly from the GPIO pins, as this can damage the Pi.

## GPIO Reference
* All practicals use BCM numbering.
