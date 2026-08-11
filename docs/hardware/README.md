# Hardware Guide

## Supported Raspberry Pi Models
- Raspberry Pi 3 Model B
- Raspberry Pi 3 Model B+
- Raspberry Pi 4 Model B
- Raspberry Pi 5

## Supported OS
- Raspberry Pi OS Bookworm (64-bit recommended)

## GPIO Pinout Reference
All practicals in this package use **BCM** (Broadcom) pin numbering.

## Common Components List
- LEDs and 330Ω Resistors
- Push Buttons
- Active Buzzer
- SG90 Servo Motor
- HC-SR04 Ultrasonic Distance Sensor
- DHT11 Temperature & Humidity Sensor
- 16x2 I2C LCD Display
- PIR Motion Sensor
- 5V Relay Module
- MCP3008 ADC with LDR (Photoresistor)
- MFRC522 RFID Reader

## ⚠️ Voltage Warnings
The Raspberry Pi GPIO pins operate at **3.3V logic levels**. 
- Never connect a 5V sensor output directly to a GPIO pin without a voltage divider or logic level converter.
- Applying 5V to any GPIO pin will permanently damage the Raspberry Pi.
