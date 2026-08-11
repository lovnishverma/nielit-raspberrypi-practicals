# Practical 3_17 — Flask GPIO Web Control

## Aim
To create a web server on the Raspberry Pi that allows users to control hardware (an LED) through a web browser.

## Learning Objectives
* Understand the basics of the HTTP protocol and web servers.
* Learn how to use the Flask web framework in Python.
* Integrate web routing with hardware control.

## Components Required
* Raspberry Pi (connected to Wi-Fi/LAN)
* LED
* 330Ω Resistor
* Breadboard & Jumper Wires
* Any device with a web browser (PC, Smartphone) on the same network

## Circuit Diagram / Hardware Connections

| Component | Raspberry Pi Pin |
| --------- | ---------------- |
| LED Anode (+)| GPIO 17 (Pin 11)|
| LED Cathode (-)| GND (Pin 6) via 330Ω Resistor|

*Note: All GPIO references use BCM numbering.*

## Software Requirements
```bash
pip install Flask gpiozero
```

## How It Works
Flask is a lightweight WSGI web application framework for Python. When the script runs, it starts a web server listening on port 5000 (`host="0.0.0.0"` allows it to accept connections from any device on the network). 
When a user navigates to the root URL (`/`), the `index` function executes and returns HTML containing the current LED state and two buttons. Clicking a button navigates to `/led/on` or `/led/off`. The `control` route captures this state, toggles the physical LED using `gpiozero`, and then redirects the user back to the index page to see the updated status.

## Running the Program
Execute the script:
```bash
python main.py
```
Find your Raspberry Pi's IP address (e.g., by running `hostname -I` in another terminal). Open a web browser on your computer or phone and navigate to `http://<YOUR_PI_IP_ADDRESS>:5000`.

## Expected Output
**Terminal:**
```
Starting Flask GPIO Web Control Practical...
LED initialized on GPIO 17.
Starting web server. Access it via http://<raspberry-pi-ip>:5000
 * Serving Flask app 'main'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.100:5000
```
**Web Browser:**
You will see a webpage with "NIELIT Raspberry Pi Web Control", the current state, and buttons to Turn ON and Turn OFF. Clicking the buttons will change the physical LED on your breadboard.

## Troubleshooting
* **Cannot reach the webpage**: Ensure the device you are browsing from is on the same Wi-Fi/LAN network as the Raspberry Pi. Double check the IP address.
* **Address already in use**: If port 5000 is occupied, you might have left a previous instance running. Stop it with `Ctrl+C`, or change the port in the code to `5001`.

## Safety Notes
* The Flask built-in server is not suitable for production deployment over the public internet due to security and scaling limitations. It is intended for local network testing and education.
