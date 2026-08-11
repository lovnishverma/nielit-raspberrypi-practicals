# Practical 3_11 — I2C LCD Display

## Aim
To interface a 16x2 Character LCD using an I2C backpack and display text on it using the Raspberry Pi.

## Learning Objectives
* Understand I2C communication protocol basics.
* Learn how to connect an I2C device to the Raspberry Pi.
* Display text, clear the screen, and format lines on a 16x2 LCD.

## Components Required
* Raspberry Pi (with power supply and internet)
* 16x2 Character LCD with PCF8574 I2C Backpack
* Jumper Wires (Female-to-Female)

## Circuit Diagram / Hardware Connections

| Component (I2C LCD) | Raspberry Pi Pin |
| ------------------- | ---------------- |
| VCC                 | 5V (Pin 2 or 4)  |
| GND                 | GND (Pin 6)      |
| SDA                 | GPIO 2 (Pin 3)   |
| SCL                 | GPIO 3 (Pin 5)   |

*Note: All GPIO references use BCM numbering.*

## Software Requirements
Ensure I2C is enabled on your Raspberry Pi (via `sudo raspi-config`).
Install required system packages and Python libraries:
```bash
sudo apt-get install python3-smbus i2c-tools
pip install nielit-rpi
```

## How It Works
The standard 16x2 LCD uses a parallel interface requiring many GPIO pins. The PCF8574 I2C backpack converts the I2C serial data into parallel signals, allowing the LCD to be controlled using only two data pins (SDA and SCL). The `nielit_rpi.displays.I2CLCD` class abstracts the low-level byte formatting (like backlight control, pulses, and nibble sending), providing easy-to-use methods like `display_string()` and `clear()`.

## Running the Program
Execute the script using Python:
```bash
python main.py
```

## Expected Output
**Terminal:**
```
Starting I2C LCD Display Practical...
LCD Initialized.
Text displayed. Keep running for 5 seconds.
Cleaning up...
Done.
```
**LCD Display:**
Line 1: "NIELIT Raspberry"
Line 2: "I2C LCD Practical"

## Troubleshooting
* **I2C Device not found**: Run `i2cdetect -y 1` in the terminal to verify the I2C address. It is usually `0x27` or `0x3F`. If different, update the address in `main.py`.
* **No text visible but backlight is on**: Adjust the contrast potentiometer on the back of the I2C backpack using a small screwdriver.
* **I2C error/Permission denied**: Ensure I2C is enabled in `raspi-config` and your user is part of the `i2c` group.

## Safety Notes
* Be careful when connecting the 5V line. Incorrect wiring can damage the Raspberry Pi's 3.3V logic pins if 5V is accidentally connected to them.
