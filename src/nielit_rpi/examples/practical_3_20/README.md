# Practical 3_20 — Smart Home Automation Capstone

## Aim
To build an integrated automated smart lighting system that turns on a light only when motion is detected *and* the room is sufficiently dark.

## Learning Objectives
* Combine multiple sensors and actuators into a single logical system.
* Apply conditional logic (AND/OR) to hardware inputs.
* Manage complex states and loops safely.

## Components Required
* Raspberry Pi
* PIR Motion Sensor (HC-SR501)
* LED & 330Ω Resistor
* (Optional) MCP3008 ADC & LDR for real ambient light sensing
* Breadboard & Jumper Wires

## Circuit Diagram / Hardware Connections

| Component | Raspberry Pi Pin |
| --------- | ---------------- |
| PIR VCC   | 5V (Pin 2)       |
| PIR OUT   | GPIO 4 (Pin 7)   |
| PIR GND   | GND (Pin 6)      |
| LED Anode | GPIO 17 (Pin 11) |
| LED Cathode| GND (Pin 9) via Resistor|

*Note: All GPIO references use BCM numbering.*

## Software Requirements
```bash
pip install nielit-rpi
```

## How It Works
This capstone project combines the concepts from Practical 3.12 (PIR) and Practical 3.13/3.17 (Output Control). The script runs a continuous loop checking two conditions: `pir.motion_detected` and `read_ambient_level()`. 
Using the logical `and` operator, the LED (representing a room light) is only turned on if someone is moving AND the ambient light is below a certain threshold (`0.35`). This mimics commercial smart home systems that save energy by not turning on lights during the day.
*(Note: `read_ambient_level()` is intentionally implemented as a stub function returning `0.2` to simulate a dark room. Students are encouraged to replace this stub with the LDR MCP3008 code from Practical 3.14 for a fully physical capstone!)*

## Running the Program
Execute the script:
```bash
python main.py
```

## Expected Output
**Terminal:**
```
Starting Smart Home Automation Capstone...
System Active: Monitoring motion and ambient light...
Press Ctrl+C to exit.
Motion detected in dark area. Turning light ON.
No motion or sufficient ambient light. Turning light OFF.
```
*The physical LED will light up when you wave your hand in front of the PIR sensor, then turn off shortly after you stop moving.*

## Troubleshooting
* **Light flashes on and off repeatedly**: The PIR sensor might be triggering itself due to power fluctuations or the time-delay dial is set too low. Adjust the potentiometers on the sensor.
* **Light never turns on**: Ensure the PIR sensor is wired correctly and detecting motion. If you modified `read_ambient_level()` to use a real LDR, check that your threshold is appropriate for your room's lighting.

## Safety Notes
* As always, ensure correct polarity when connecting the LED, and double-check that 5V components (like the PIR power) are not accidentally connected directly to GPIO data pins.
