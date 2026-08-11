# Installation Guide

## Prerequisites
- A supported Raspberry Pi running Raspberry Pi OS Bookworm.
- Python 3.9 or newer installed.
- Internet access for installing packages.

## Enabling Interfaces
Before running practicals, you must enable required hardware interfaces via `raspi-config`:
```bash
sudo raspi-config
```
Navigate to **Interface Options** and enable:
- I2C (for LCD)
- SPI (for MCP3008 and RFID)
- Camera (if applicable)

## Virtual Environment Setup
It is highly recommended to use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Installing from Source
Clone the repository and install in editable mode:
```bash
git clone https://github.com/nielit/raspberrypi-practicals.git
cd raspberrypi-practicals
pip install -e .
```

## Installing from Wheel
If you have built the `.whl` file:
```bash
pip install nielit_rpi-1.0.0-py3-none-any.whl
```

## Optional Dependency Groups
Install extra dependencies for specific practicals:
```bash
pip install -e .[web]   # For Flask practicals
pip install -e .[mqtt]  # For MQTT practicals
pip install -e .[all]   # Install everything
```
