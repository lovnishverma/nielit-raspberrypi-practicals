# Practical 3_12 — PIR Motion Detection

## Aim
To detect motion using a PIR (Passive Infrared) sensor and trigger events.

## Learning Objectives
* Understand how PIR sensors detect infrared radiation changes.
* Learn to use event-driven programming (callbacks) for sensor inputs.
* Practice clean GPIO resource management.

## Components Required
* Raspberry Pi
* PIR Motion Sensor (HC-SR501)
* Jumper Wires (Female-to-Female)

## Circuit Diagram / Hardware Connections

| Component (HC-SR501) | Raspberry Pi Pin |
| -------------------- | ---------------- |
| VCC                  | 5V (Pin 2 or 4)  |
| OUT / DATA           | GPIO 4 (Pin 7)   |
| GND                  | GND (Pin 6)      |

*Note: All GPIO references use BCM numbering.*

## Software Requirements
```bash
pip install nielit-rpi
```

## How It Works
The HC-SR501 PIR sensor measures changes in infrared light across its field of view. When a warm body (like a human) moves, the sensor detects the change and pulls its OUT pin HIGH (3.3V). The script uses the `nielit_rpi.sensors.PIRSensor` wrapper (built on `gpiozero.MotionSensor`) to monitor GPIO 4 asynchronously. Instead of constantly polling the sensor in a loop, it uses callbacks (`when_motion` and `when_no_motion`) which execute automatically when state changes occur. The `pause()` function keeps the main thread alive without consuming CPU resources.

## Running the Program
Execute the script:
```bash
python main.py
```

## Expected Output
**Terminal:**
```
Starting PIR Motion Detection Practical...
Monitoring GPIO 4 for motion...
Press Ctrl+C to exit.
Motion detected!
No motion.
Motion detected!
```

## Troubleshooting
* **Sensor is always triggered / never triggers**: Adjust the sensitivity and time-delay potentiometers on the sensor module.
* **False positives**: Keep the sensor away from direct sunlight, heating vents, or Wi-Fi routers, as these can cause interference or temperature fluctuations.
* **Delayed response**: Reduce the time-delay potentiometer (turn counter-clockwise).

## Safety Notes
* The PIR sensor runs on 5V but its data output is 3.3V, making it safe to connect directly to the Raspberry Pi GPIO pins.
