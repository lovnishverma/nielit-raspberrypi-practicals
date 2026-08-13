# 🍓 NIELIT Raspberry Pi Practicals

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/nielit-raspberrypi-practicals.svg?color=blue&style=flat-square)](https://pypi.org/project/nielit-raspberrypi-practicals/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/nielit-raspberrypi-practicals.svg?color=orange&style=flat-square)](https://pypi.org/project/nielit-raspberrypi-practicals/)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue?style=flat-square)](https://pypi.org/project/nielit-raspberrypi-practicals/)
[![License](https://img.shields.io/badge/license-NIELIT%20Ropar-green?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi%203%20%7C%204%20%7C%205-red?style=flat-square)](https://www.raspberrypi.com/)
[![CI Status](https://img.shields.io/github/actions/workflow/status/lovnishverma/nielit-raspberrypi-practicals/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/lovnishverma/nielit-raspberrypi-practicals/actions)
[![Docs](https://img.shields.io/badge/docs-Interactive%20Manual-purple?style=flat-square)](https://lovnishverma.github.io/nielit-raspberrypi-practicals/)

**A comprehensive, production-grade Python package and interactive laboratory manual containing 20 structured Raspberry Pi practical programs developed for the NIELIT curriculum.**

[📦 PyPI Package](https://pypi.org/project/nielit-raspberrypi-practicals/) • [🌐 Interactive Documentation](https://lovnishverma.github.io/nielit-raspberrypi-practicals/) • [💻 GitHub Repository](https://github.com/lovnishverma/nielit-raspberrypi-practicals) • [🐛 Report Issue](https://github.com/lovnishverma/nielit-raspberrypi-practicals/issues)

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Installation Guide](#-installation-guide)
  - [Standard Installation](#1-standard-installation)
  - [Full Hardware Installation](#2-full-hardware-installation)
  - [Raspberry Pi OS (Bookworm) Virtual Environment](#3-raspberry-pi-os-bookworm-setup)
  - [Enabling Hardware Interfaces (I2C, SPI, UART)](#4-enabling-hardware-interfaces)
- [Command-Line Interface (`nielit-rpi`)](#-command-line-interface-nielit-rpi)
  - [List Practicals](#1-list-all-practicals)
  - [Check Hardware & Dependencies](#2-check-hardware--dependencies)
  - [Show Practical Details](#3-show-practical-details)
  - [Run a Practical](#4-run-a-practical-program)
  - [Export Examples to Local Directory](#5-export-examples-for-experimentation)
- [Master Practical Index (3.1 – 3.20)](#-master-practical-index-31--320)
- [Python Library API Reference](#-python-library-api-reference)
  - [GPIO Control (`nielit_rpi.gpio`)](#1-gpio-control-nielit_rpigpio)
  - [Sensors (`nielit_rpi.sensors`)](#2-sensors-nielit_rpisensors)
  - [Actuators (`nielit_rpi.actuators`)](#3-actuators-nielit_rpiactuators)
  - [Displays (`nielit_rpi.displays`)](#4-displays-nielit_rpidisplays)
  - [Communication & IoT (`nielit_rpi.communication`)](#5-communication--iot-nielit_rpicommunication)
  - [Data Logging (`nielit_rpi.storage`)](#6-telemetry--data-logging-nielit_rpistorage)
  - [Web Interfaces (`nielit_rpi.networking`)](#7-web-interfaces-nielit_rpinetworking)
  - [Utilities & Diagnostics (`nielit_rpi.utilities`)](#8-utilities--diagnostics-nielit_rpiutilities)
- [Raspberry Pi 40-Pin GPIO Reference & Safety](#-raspberry-pi-40-pin-gpio-reference--safety)
- [Testing & Quality Assurance](#-testing--quality-assurance)
- [Troubleshooting & FAQ](#-troubleshooting--faq)
- [License & Authors](#-license--authors)

---

## 🌟 Overview

The `nielit-raspberrypi-practicals` library provides a unified, object-oriented, and student-friendly Python framework covering all **20 official NIELIT Raspberry Pi practicals** (Practicals 3.1 through 3.20).

Each practical is accompanied by:
- **Clean Python Code**: Full PEP 8 compliance, explicit type hints, and robust error handling.
- **Graceful Lifecycle Management**: Context managers (`with` statements) and automatic cleanup of GPIO pins to protect hardware.
- **Standalone Documentation**: Detailed READMEs with circuit schematics, components, pinout tables, and troubleshooting steps.
- **Interactive Manual**: Modern HTML5 laboratory manual with real-time pin tracing and 1-click code copying.

---

## ✨ Key Features

- 🎯 **Complete Curriculum Coverage**: 20 practicals from basic LED blinking and analog sensor reading to MQTT IoT telemetry and Flask Web servers.
- 🛡️ **Hardware Safe**: Built-in 3.3V logic checks, software pull-up resistors, debounce filtering, and fail-safe cleanup handlers.
- ⚡ **CLI Companion**: The `nielit-rpi` command-line utility lets students inspect diagnostics, browse practicals, and run or export experiments instantly.
- 🌐 **Modern Packaging**: Fully compatible with Python 3.9 through 3.12 on Raspberry Pi OS (Bookworm & Bullseye).
- 🧩 **Modular OOP Architecture**: Every hardware component has a dedicated, reusable controller class.

---

## 📦 Installation Guide

### 1. Standard Installation
Installs core GPIO and basic sensor support:
```bash
pip install nielit-raspberrypi-practicals
```

### 2. Full Hardware Installation
Installs all peripheral drivers including I2C LCD (`smbus2`), SPI RFID (`mfrc522`, `spidev`), DHT sensors (`adafruit-circuitpython-dht`), MQTT (`paho-mqtt`), and Web server (`flask`):
```bash
pip install "nielit-raspberrypi-practicals[all]"
```

### 3. Raspberry Pi OS (Bookworm) Setup
On newer Raspberry Pi OS releases (Debian Bookworm), Python enforces **PEP 668** (externally managed environment). Use a virtual environment:

```bash
# Create a virtual environment with access to system packages
python3 -m venv ~/nielit-env --system-site-packages

# Activate the virtual environment
source ~/nielit-env/bin/activate

# Install package
pip install --upgrade "nielit-raspberrypi-practicals[all]"
```

> **Tip:** Add `source ~/nielit-env/bin/activate` to your `~/.bashrc` to activate the environment automatically upon terminal launch.

### 4. Enabling Hardware Interfaces
Ensure that I2C, SPI, and Serial interfaces are enabled on your Raspberry Pi:

```bash
# Enable I2C interface
sudo raspi-config nonint do_i2c 0

# Enable SPI interface
sudo raspi-config nonint do_spi 0

# Enable Serial UART
sudo raspi-config nonint do_serial_hw 0
```

---

## 🛠️ Command-Line Interface (`nielit-rpi`)

The package includes a powerful command-line tool named `nielit-rpi`.

### 1. List All Practicals
Display a formatted table of all 20 practicals with their hardware requirements and difficulty ratings:
```bash
nielit-rpi list
```
**Output Preview:**
```text
ID     | Title                          | Hardware             | Difficulty     
--------------------------------------------------------------------------------
3_1    | System Information             | RPi only             | Beginner       
3_2    | GPIO LED Output                | LED + resistor       | Beginner       
3_3    | Push Button Input              | Push button          | Beginner       
3_4    | Button Controlled LED          | Button + LED         | Beginner       
3_5    | Traffic Light Controller       | 3 LEDs               | Beginner       
3_6    | PWM LED Brightness             | LED                  | Beginner       
...
3_20   | Smart Home Capstone            | PIR + LED            | Advanced       
```

---

### 2. Check Hardware & Dependencies
Run an automated diagnostic check on your Raspberry Pi system, kernel, Python environment, and enabled hardware interfaces (I2C, SPI):
```bash
nielit-rpi check
```
**Output Preview:**
```text
--- System Check ---
Hostname: raspberrypi
Python version: 3.11.2
Model: Raspberry Pi 4 Model B Rev 1.4

--- Dependencies ---
[OK] gpiozero is installed
[OK] smbus2 is installed
[OK] paho-mqtt is installed
[OK] flask is installed

--- Hardware Interfaces ---
[OK] I2C interface is enabled (/dev/i2c-1 found)
[OK] SPI interface is enabled (/dev/spidev0.0 found)
```

---

### 3. Show Practical Details
Retrieve the aim, hardware components, circuit wiring, and safety notes for any practical:
```bash
nielit-rpi info 3_2
```
```bash
nielit-rpi info 3_10
```

---

### 4. Run a Practical Program
Execute any practical directly by its ID from any folder:
```bash
# Run system diagnostics
nielit-rpi run 3_1

# Run LED blinking practical
nielit-rpi run 3_2

# Run DHT11 temperature & humidity monitoring
nielit-rpi run 3_10
```

---

### 5. Export Examples for Experimentation
Export all 20 editable practical scripts into your current project folder:
```bash
nielit-rpi export-examples
```
Or specify a custom directory:
```bash
nielit-rpi export-examples --dest my_practicals
```
Students can then navigate into any folder and run or modify `main.py`:
```bash
cd examples/practical_3_2
python main.py
```

---

## 📚 Master Practical Index (3.1 – 3.20)

| ID | Practical Title | Hardware Required | BCM Pins | Category | Difficulty | CLI Command |
|:---|:---|:---|:---|:---|:---|:---|
| **3_1** | System Diagnostics & Info | Raspberry Pi only | — | System | Beginner | `nielit-rpi run 3_1` |
| **3_2** | GPIO LED Output | LED, 330Ω Resistor | GPIO 17 | GPIO Output | Beginner | `nielit-rpi run 3_2` |
| **3_3** | Push Button Input | Push Button | GPIO 18 | GPIO Input | Beginner | `nielit-rpi run 3_3` |
| **3_4** | Button-Controlled LED | LED, Button, 330Ω Resistor | GPIO 17, 18 | Interactive | Beginner | `nielit-rpi run 3_4` |
| **3_5** | Traffic Light Controller | Red, Yellow, Green LEDs | GPIO 17, 27, 22 | State Machine | Beginner | `nielit-rpi run 3_5` |
| **3_6** | PWM LED Brightness | LED, 330Ω Resistor | GPIO 18 (PWM) | PWM Analog | Beginner | `nielit-rpi run 3_6` |
| **3_7** | Active Buzzer Alert | Active Buzzer | GPIO 23 | Audio Alert | Beginner | `nielit-rpi run 3_7` |
| **3_8** | Servo Motor Angle Control | SG90 Micro Servo, Ext 5V | GPIO 18 (PWM) | Actuators | Intermediate | `nielit-rpi run 3_8` |
| **3_9** | HC-SR04 Ultrasonic Distance | HC-SR04, 1kΩ + 2kΩ Divider | GPIO 23, 24 | Sensors | Intermediate | `nielit-rpi run 3_9` |
| **3_10** | DHT11 Temp & Humidity | DHT11 Sensor, 10kΩ Pull-up | GPIO 4 | Sensors | Intermediate | `nielit-rpi run 3_10` |
| **3_11** | I2C 16x2 LCD Display | 16x2 LCD with PCF8574 | GPIO 2 (SDA), 3 (SCL) | Displays | Intermediate | `nielit-rpi run 3_11` |
| **3_12** | PIR Motion Detection | HC-SR501 PIR Sensor | GPIO 4 | Sensors | Intermediate | `nielit-rpi run 3_12` |
| **3_13** | Relay Module Control | 5V Relay Module, AC Load | GPIO 26 | Actuators | Intermediate | `nielit-rpi run 3_13` |
| **3_14** | LDR Light Sensor via ADC | LDR, 10kΩ Resistor, MCP3008 | SPI (GPIO 8..11) | ADC / SPI | Intermediate | `nielit-rpi run 3_14` |
| **3_15** | MFRC522 RFID Card Reader | RC522 RFID Module, Cards | SPI (GPIO 8..11, 25) | RFID / SPI | Advanced | `nielit-rpi run 3_15` |
| **3_16** | SQLite Sensor Data Logger | Raspberry Pi only | — | Storage | Intermediate | `nielit-rpi run 3_16` |
| **3_17** | Flask GPIO Web Controller | LED, LAN Network | GPIO 17 | Web / IoT | Advanced | `nielit-rpi run 3_17` |
| **3_18** | MQTT Sensor Telemetry Pub | Network, MQTT Broker | — | IoT / MQTT | Advanced | `nielit-rpi run 3_18` |
| **3_19** | MQTT Remote LED Sub | LED, Network, MQTT Broker | GPIO 17 | IoT / MQTT | Advanced | `nielit-rpi run 3_19` |
| **3_20** | Smart Home Energy Capstone | PIR Sensor, LED, Relay | GPIO 4, 17, 26 | Integrated | Advanced | `nielit-rpi run 3_20` |

---

## 💻 Python Library API Reference

Import components into your own custom projects with `import nielit_rpi`:

### 1. GPIO Control (`nielit_rpi.gpio`)

#### LED Control
```python
from nielit_rpi.gpio import LEDController
import time

# Use as a context manager for automatic cleanup
with LEDController(pin=17) as led:
    led.on()
    time.sleep(1)
    led.off()
    led.blink(on_time=0.5, off_time=0.5, n=5)
```

#### Push Button with Callbacks
```python
from nielit_rpi.gpio import ButtonReader

btn = ButtonReader(pin=18, pull_up=True, bounce_time=0.05)

btn.when_pressed = lambda: print("Button Pressed!")
btn.when_released = lambda: print("Button Released!")
btn.wait_for_press(timeout=10)
btn.close()
```

#### PWM Brightness & Buzzer
```python
from nielit_rpi.gpio import PWMLEDController, BuzzerController

# Fade LED
with PWMLEDController(pin=18) as pwm_led:
    pwm_led.pulse(fade_in_time=1.0, fade_out_time=1.0, n=3)

# Buzzer alert
with BuzzerController(pin=23) as buzzer:
    buzzer.beep(on_time=0.1, off_time=0.1, n=3)
```

---

### 2. Sensors (`nielit_rpi.sensors`)

#### Ultrasonic Distance (HC-SR04)
```python
from nielit_rpi.sensors import UltrasonicSensor

sensor = UltrasonicSensor(trigger_pin=23, echo_pin=24, max_distance=4.0)
print(f"Current Distance: {sensor.distance_cm:.2f} cm")
sensor.close()
```

#### DHT11 / DHT22 Temperature & Humidity
```python
import board
from nielit_rpi.sensors import DHTSensor

# Note: Uses Adafruit CircuitPython board pin definition
with DHTSensor(pin=board.D4, sensor_type="DHT11") as dht:
    reading = dht.read()
    print(f"Temperature: {reading['temperature']}°C | Humidity: {reading['humidity']}%")
```

#### PIR Motion Sensor
```python
from nielit_rpi.sensors import PIRSensor

with PIRSensor(pin=4) as pir:
    if pir.motion_detected:
        print("Motion detected!")
```

#### Analog LDR Light Sensor (via MCP3008 ADC)
```python
from nielit_rpi.sensors import LDRSensor

with LDRSensor(channel=0) as ldr:
    print(f"Raw Value: {ldr.value:.4f} | Voltage: {ldr.voltage:.2f}V")
```

---

### 3. Actuators (`nielit_rpi.actuators`)

#### 5V Relay Control
```python
from nielit_rpi.actuators import RelayController

with RelayController(pin=26, active_high=True) as relay:
    relay.on()   # Turn on connected load
    relay.off()  # Turn off load
    relay.toggle()
```

#### Servo Motor Control
```python
from nielit_rpi.actuators import ServoController

with ServoController(pin=18, min_angle=-90, max_angle=90) as servo:
    servo.angle = 0    # Center position
    servo.angle = 90   # Maximum clockwise
    servo.angle = -90  # Maximum counter-clockwise
    servo.sweep(start=-90, end=90, step=15, delay=0.1)
```

---

### 4. Displays (`nielit_rpi.displays`)

#### I2C 16x2 LCD
```python
from nielit_rpi.displays import I2CLCD

with I2CLCD(address=0x27, bus_number=1) as lcd:
    lcd.clear()
    lcd.write_string("NIELIT Ropar", line=1)
    lcd.write_string("IoT Laboratory", line=2)
```

---

### 5. Communication & IoT (`nielit_rpi.communication`)

#### RC522 RFID Reader
```python
from nielit_rpi.communication import RFIDReader

with RFIDReader() as rfid:
    print("Hold an RFID card near the reader...")
    card_id, text = rfid.read()
    print(f"Card UID: {card_id} | Data: {text}")
```

#### MQTT Telemetry Publisher & Subscriber
```python
from nielit_rpi.communication import MQTTPublisher, MQTTSubscriber

# Publish reading
pub = MQTTPublisher(broker="broker.hivemq.com", port=1883, topic="nielit/rpi/sensor")
pub.connect()
pub.publish({"temperature": 25.4, "humidity": 60})
pub.disconnect()

# Subscribe to commands
def on_message(client, userdata, msg):
    print(f"Received payload: {msg.payload.decode()}")

sub = MQTTSubscriber(broker="broker.hivemq.com", port=1883, topic="nielit/rpi/led", on_message_callback=on_message)
sub.connect()
sub.start()
```

---

### 6. Telemetry & Data Logging (`nielit_rpi.storage`)

#### SQLite Sensor Logger
```python
from nielit_rpi.storage import SensorDataLogger

logger = SensorDataLogger(db_path="telemetry.db", table_name="climate")
logger.create_table(columns={"temp": "REAL", "humidity": "REAL", "status": "TEXT"})

# Log reading with automatic timestamp
logger.log_reading(temp=24.5, humidity=58.2, status="OPTIMAL")

# Query recent records
rows = logger.get_readings(limit=10)
for row in rows:
    print(row)
logger.close()
```

---

### 7. Web Interfaces (`nielit_rpi.networking`)

#### Web-Based GPIO Controller (Flask)
```python
from nielit_rpi.networking import create_gpio_web_app

app = create_gpio_web_app(led_pin=17)
# Run server on port 5000 accessible across the local network
app.run(host="0.0.0.0", port=5000, debug=False)
```

---

### 8. Utilities & Diagnostics (`nielit_rpi.utilities`)

```python
from nielit_rpi.utilities import get_system_info, cleanup_devices

# Fetch full system diagnostics dict
info = get_system_info()
print(f"RPi Model : {info.get('model')}")
print(f"Python    : {info.get('python_version')}")
print(f"Disk Free : {info.get('disk_usage', {}).get('free_gb')} GB")
```

---

## ⚡ Raspberry Pi 40-Pin GPIO Reference & Safety

```text
                           3.3V Power [01] [02] 5V Power
       (I2C1 SDA) GPIO 2 / Pin 3  [03] [04] 5V Power
       (I2C1 SCL) GPIO 3 / Pin 5  [05] [06] Ground
     (GPCLK0)     GPIO 4 / Pin 7  [07] [08] GPIO 14 / Pin 8  (UART TXD)
                  Ground / Pin 9  [09] [10] GPIO 15 / Pin 10 (UART RXD)
     (SPI1_CE1)  GPIO 17 / Pin 11 [11] [12] GPIO 18 / Pin 12 (PWM0)
                 GPIO 27 / Pin 13 [13] [14] Ground
                 GPIO 22 / Pin 15 [15] [16] GPIO 23 / Pin 16
                3.3V Power [17] [18] GPIO 24 / Pin 18
     (SPI0 MOSI) GPIO 10 / Pin 19 [19] [20] Ground
     (SPI0 MISO)  GPIO 9 / Pin 21 [21] [22] GPIO 25 / Pin 22
     (SPI0 SCLK) GPIO 11 / Pin 23 [23] [24] GPIO 8 / Pin 24  (SPI0 CE0)
                  Ground / Pin 25 [25] [26] GPIO 7 / Pin 26  (SPI0 CE1)
     (I2C0 ID_SD) GPIO 0 / Pin 27 [27] [28] GPIO 1 / Pin 28  (I2C0 ID_SC)
                  GPIO 5 / Pin 29 [29] [30] Ground
                  GPIO 6 / Pin 31 [31] [32] GPIO 12 / Pin 32 (PWM0)
                 GPIO 13 / Pin 33 [33] [34] Ground
     (SPI1 MISO) GPIO 19 / Pin 35 [35] [36] GPIO 16 / Pin 36 (SPI1 CE2)
                 GPIO 26 / Pin 37 [37] [38] GPIO 20 / Pin 38 (SPI1 MOSI)
                  Ground / Pin 39 [39] [40] GPIO 21 / Pin 40 (SPI1 SCLK)
```

### ⚠️ Essential Electrical Safety Rules:
1. **3.3V Logic Limit**: Raspberry Pi GPIO pins operate strictly at **3.3V**. Connecting 5V directly to a GPIO input pin **will permanently damage the SoC**. Always use a resistor voltage divider (e.g. 1kΩ + 2kΩ on HC-SR04 Echo) or a logic level shifter.
2. **Current Limiting**: Maximum current draw per GPIO pin is **16 mA** (and total < 50 mA across all pins). Always use a 330Ω resistor with LEDs.
3. **Inductive Loads & Relays**: Never drive motors, relays, or solenoids directly from GPIO pins. Use transistor/MOSFET driver stages or opto-isolated relay boards.
4. **Servo Power Isolation**: High-torque servos create voltage drops. Power servos with an external 5V DC supply with shared ground.

---

## 🧪 Testing & Quality Assurance

The package includes a comprehensive test suite with 100% hardware-mocked unit tests that run on Linux, Windows, macOS, and CI pipelines without requiring physical Raspberry Pi hardware.

```bash
# Clone the repository
git clone https://github.com/lovnishverma/nielit-raspberrypi-practicals.git
cd nielit-raspberrypi-practicals

# Install development dependencies
pip install -e ".[dev,all]"

# Run full pytest test suite
pytest tests/ -v
```

---

## ❓ Troubleshooting & FAQ

### Q1: `Permission denied: /dev/gpiomem` or `No access to /dev/mem`
**Fix:** Add your user to the `gpio` group and reboot:
```bash
sudo usermod -a -G gpio,i2c,spi $USER
sudo reboot
```

### Q2: I2C LCD not displaying anything (Blank or Black Squares)
**Fix:** 
1. Check the potentiometer on the back of the I2C backpack and turn it with a small screwdriver to adjust display contrast.
2. Verify I2C address using `i2cdetect -y 1` (default is usually `0x27` or `0x3F`).

### Q3: DHT11 Sensor gives `RuntimeError: A full buffer was not returned`
**Fix:** DHT sensors use time-sensitive bit-banging. Occasional timeouts are normal. The `DHTSensor.read()` method in this library automatically retries up to 3 times. Ensure a 10kΩ pull-up resistor is placed between VCC and Data pin.

### Q4: `error: externally-managed-environment` when running `pip install`
**Fix:** You are on Debian Bookworm. Create and activate a Python virtual environment as shown in the [Installation Guide](#3-raspberry-pi-os-bookworm-setup).

---

## 📄 License & Authors

- **Organization:** [National Institute of Electronics & Information Technology (NIELIT), Ropar](https://nielit.gov.in/ropar/)
- **License:** NIELIT Ropar License. Copyright (c) 2026 NIELIT Ropar.
- **Maintainer:** Lovnish Verma ([@lovnishverma](https://github.com/lovnishverma))
- **Email:** `princelv84@gmail.com`

---

<div align="center">
<b>National Institute of Electronics and Information Technology (NIELIT), Ropar</b><br>
An Autonomous Scientific Society under the administrative control of the Ministry of Electronics & Information Technology (MeitY), Government of India.
</div>
