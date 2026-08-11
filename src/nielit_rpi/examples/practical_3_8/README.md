# Practical 3_8 — Servo Motor Control

## Aim
To control the precise angular position of a servo motor.

## Learning Objectives
* Understand how PWM signals dictate servo positioning.
* Learn to use specific pulse width timings for SG90 servos.
* Practice safe hardware power distribution.

## Components Required
* Raspberry Pi
* 1x SG90 Micro Servo Motor
* External 5V Power Supply
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* Servo VCC (Red) -> External 5V Power Supply (+)
* Servo GND (Brown) -> External GND (-) AND Raspberry Pi GND
* Servo Signal (Orange) -> GPIO 18

## Software Requirements
* `nielit_rpi` library

## How It Works
The script initializes a `ServoController` which utilizes pulse-width modulation to set the angle of the servo motor. By sending a specific pulse width between 0.5ms (-90 degrees) and 2.5ms (90 degrees), the servo shaft rotates to the desired position.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
Controlling Servo on GPIO 18.
Ensure the servo has an external 5V power supply.
Moving to angle: -90 degrees
Moving to angle: -45 degrees
...
```

## Troubleshooting
* **Servo twitches but doesn't move properly**: Power supply issue. Do not power servos directly from the Pi's 3.3V or 5V rail as they draw too much current. Use an external supply.
* **Servo moves to wrong angles**: You may need to calibrate the `min_pulse_width` and `max_pulse_width` for your specific brand of servo.
* **No movement**: Ensure the grounds of the external power supply and the Raspberry Pi are connected together.

## Safety Notes
* **Never draw power for motors directly from the Raspberry Pi GPIO pins**. Always use a suitable external power supply.

## GPIO Reference
* All practicals use BCM numbering.
