# Practical 3_13 — Relay Control

## Aim
To control a high-power device safely using a relay module from the Raspberry Pi.

## Learning Objectives
* Understand the purpose and mechanics of a relay (electromagnetic switch).
* Learn how to control outputs programmatically to switch external circuits.
* Emphasize electrical safety and isolation.

## Components Required
* Raspberry Pi
* 3.3V or 5V-compatible Relay Module (with internal optocoupler/transistor)
* Jumper Wires
* (Optional) Low voltage DC circuit to switch (e.g., a 9V battery and DC motor)

## Circuit Diagram / Hardware Connections

| Component (Relay Module) | Raspberry Pi Pin |
| ------------------------ | ---------------- |
| VCC                      | 5V or 3.3V       |
| GND                      | GND (Pin 6)      |
| IN (Control)             | GPIO 17 (Pin 11) |

*Note: All GPIO references use BCM numbering. The VCC pin depends on your specific relay module's logic level requirements.*

## Software Requirements
```bash
pip install nielit-rpi
```

## How It Works
A relay is an electromechanical switch that allows a low-power signal (from the Raspberry Pi) to control a high-power circuit. The Raspberry Pi GPIO pins can only provide 3.3V at a very low current. The relay module contains a transistor (and sometimes an optocoupler) that amplifies this small signal to energize a coil, which magnetically closes a switch in the higher-power circuit. The `nielit_rpi.actuators.RelayController` manages the state (ON/OFF) of the GPIO pin.

## Running the Program
Execute the script:
```bash
python main.py
```

## Expected Output
**Terminal:**
```
Starting Relay Control Practical...
Turning relay ON...
Turning relay OFF...
Cleaning up GPIO resources...
Done.
```
*You should also hear a distinct "click" sound from the relay when it switches ON and OFF.*

## Troubleshooting
* **No click sound**: Ensure the relay module VCC and GND are connected properly. If it's a 5V relay, the 3.3V GPIO signal might not be enough to trigger it depending on the module's design.
* **Relay turns on when program says OFF**: Some relay modules are "Active Low". If this happens, change `active_high=True` to `active_high=False` in your code.

## Safety Notes
* **WARNING: NEVER CONNECT MAINS VOLTAGE (120V/240V AC) TO YOUR BREADBOARD OR RASPBERRY PI.** 
* Mains electricity is lethal. Always use: RPi GPIO → Relay Module → External Load. 
* For this practical, only switch low-voltage DC loads (e.g., 5V-12V DC).
