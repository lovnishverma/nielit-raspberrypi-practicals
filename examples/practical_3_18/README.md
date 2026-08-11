# Practical 3_18 — MQTT Publisher

## Aim
To send (publish) simulated sensor data to a remote MQTT broker, introducing the core concepts of IoT messaging.

## Learning Objectives
* Understand the Publish/Subscribe messaging model.
* Learn how to structure data using JSON.
* Transmit telemetry data to a cloud/public broker.

## Components Required
* Raspberry Pi (with Internet connection)

## Circuit Diagram / Hardware Connections
No hardware is required for this practical, as it relies purely on network communication and software simulation.

## Software Requirements
```bash
pip install paho-mqtt nielit-rpi
```

## How It Works
MQTT is a lightweight messaging protocol designed for constrained devices and low-bandwidth networks. It operates on a Publish/Subscribe model. A device (Publisher) sends data to a central server (Broker) labeled with a specific "Topic". Other devices (Subscribers) listening to that topic receive the message. 
This script connects to the public `test.mosquitto.org` broker and publishes JSON-formatted messages to the topic `nielit/rpi/sensor`. The `nielit_rpi.communication.MQTTPublisher` wraps the Paho MQTT client for simplified connectivity.

## Running the Program
Execute the script:
```bash
python main.py
```
You can override the default broker settings using environment variables:
```bash
MQTT_TOPIC="my/custom/topic" python main.py
```

## Expected Output
**Terminal:**
```
Starting MQTT Publisher Practical...
Broker: test.mosquitto.org:1883
Topic: nielit/rpi/sensor
Connected. Publishing messages...
Published: {"device": "raspberry-pi", "value": 0}
Published: {"device": "raspberry-pi", "value": 1}
...
Disconnecting from broker...
Done.
```

## Troubleshooting
* **Connection Refused or Timeout**: Ensure your Raspberry Pi is connected to the internet. Some corporate or university networks block port 1883. You may need to use a different port (like 8883 for TLS) or test on a mobile hotspot.
* **No messages received on the other end**: Ensure that the subscriber is listening to the exact same topic (`nielit/rpi/sensor`) and connected to the same broker (`test.mosquitto.org`).

## Safety Notes
* The default broker (`test.mosquitto.org`) is public. Anyone can read the data you publish if they know the topic. Do not send sensitive or private information over unencrypted, public MQTT channels.
