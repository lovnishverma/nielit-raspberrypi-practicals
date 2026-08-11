# Practical 3_9 — HC-SR04 Distance Measurement

## Aim
To measure the distance to an object using an HC-SR04 ultrasonic sensor.

## Learning Objectives
* Interface an ultrasonic sensor with the Raspberry Pi.
* Understand the use of voltage dividers for safe signal levels.
* Calculate distance based on time-of-flight of sound waves.

## Components Required
* Raspberry Pi
* 1x HC-SR04 Ultrasonic Sensor
* 1x 1kΩ Resistor
* 1x 2kΩ Resistor (or 2.2kΩ)
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* Sensor VCC -> 5V Pin on Raspberry Pi
* Sensor GND -> GND
* Sensor TRIG -> GPIO 23
* Sensor ECHO -> Voltage Divider -> GPIO 24
  * Connect ECHO to a 1kΩ resistor.
  * Connect the other end of the 1kΩ resistor to GPIO 24 AND a 2kΩ resistor.
  * Connect the other end of the 2kΩ resistor to GND.

## Software Requirements
* `nielit_rpi` library

## How It Works
The sensor emits an ultrasonic pulse via the TRIG pin and measures the time it takes for the echo to return to the ECHO pin. The library abstracts this time-of-flight calculation and returns the distance in meters. Because the sensor operates at 5V, a voltage divider is strictly required on the ECHO pin to step down the returning signal to a safe 3.3V for the Pi's GPIO.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
Ultrasonic Distance Measurement.
Trigger: GPIO 23, Echo: GPIO 24
Press Ctrl+C to stop.
Distance: 15.2 cm
```

## Troubleshooting
* **Inaccurate or wildly fluctuating readings**: Ensure your wires are securely connected. Avoid placing the sensor near soft, sound-absorbing materials.
* **Sensor returns 100% / max distance constantly**: Check your voltage divider wiring. If the ECHO pin is not wired correctly, the Pi will not register the return pulse.
* **Script crashes on startup**: Double-check that your user permissions allow GPIO access.

## Safety Notes
* **CRITICAL**: You MUST use a voltage divider on the ECHO pin. Connecting a 5V signal directly to the Raspberry Pi's GPIO pins will damage the board permanently.

## GPIO Reference
* All practicals use BCM numbering.
