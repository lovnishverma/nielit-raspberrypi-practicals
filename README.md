# NIELIT Raspberry Pi Practicals

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A professional Python package containing 20 Raspberry Pi practical programs developed for the NIELIT curriculum.

## Features
- **Comprehensive**: 20 distinct practical programs covering basic GPIO to advanced IoT concepts.
- **Hardware Agnostic**: Tested on Raspberry Pi 3, 4, and 5 running Raspberry Pi OS (Bookworm).
- **Educational**: Code is structured for learning, featuring clear type hints, docstrings, and robust error handling.
- **Modern Python**: Built with modern packaging (`pyproject.toml`) and tooling.
- **CLI Utility**: Built-in command-line tool to list, query, and run practicals.

## Quick Start

### Installation

Requires Python 3.9+. It's recommended to use a virtual environment.

```bash
# Basic installation
pip install nielit-raspberrypi-practicals

# Install with all optional hardware dependencies
pip install nielit-raspberrypi-practicals[all]
```

### Basic Usage

List all available practicals:
```bash
nielit-rpi list
```

Check system capability:
```bash
nielit-rpi check
```

Run a specific practical:
```bash
nielit-rpi run 3_2
```

## Practical Index

| # | Title | Hardware | Difficulty |
|---|---|---|---|
| 3_1 | System Information | RPi only | Beginner |
| 3_2 | GPIO LED Output | LED + resistor | Beginner |
| 3_3 | Push Button Input | Push button | Beginner |
| 3_4 | Button Controlled LED | Button + LED | Beginner |
| 3_5 | Traffic Light Controller | 3 LEDs | Beginner |
| 3_6 | PWM LED Brightness | LED | Beginner |
| 3_7 | Buzzer Alert | Active buzzer | Beginner |
| 3_8 | Servo Motor Control | SG90 servo | Intermediate |
| 3_9 | HC-SR04 Distance | HC-SR04 sensor | Intermediate |
| 3_10 | DHT11 Temp & Humidity | DHT11 sensor | Intermediate |
| 3_11 | I2C LCD Display | 16x2 I2C LCD | Intermediate |
| 3_12 | PIR Motion Detection | PIR sensor | Intermediate |
| 3_13 | Relay Control | Relay module | Intermediate |
| 3_14 | LDR + MCP3008 ADC | MCP3008 + LDR | Intermediate |
| 3_15 | MFRC522 RFID | MFRC522 module | Advanced |
| 3_16 | SQLite Sensor Logger | RPi only | Intermediate |
| 3_17 | Flask GPIO Web Control | LED + LAN | Advanced |
| 3_18 | MQTT Publisher | Network | Advanced |
| 3_19 | MQTT Subscriber + GPIO | LED + MQTT | Advanced |
| 3_20 | Smart Home Capstone | PIR + LED | Advanced |

## Supported Environment
- **Hardware**: Raspberry Pi 3 / 4 / 5
- **OS**: Raspberry Pi OS (Bookworm)
- **Python**: 3.9+

## Development Setup

```bash
git clone https://github.com/nielit/nielit-raspberrypi-practicals.git
cd nielit-raspberrypi-practicals
pip install -e .[dev,all]
```

## Testing

```bash
pytest
```

## License
MIT License. Copyright (c) 2024 NIELIT.
