# Practical 3_19 — MQTT Subscriber + GPIO

## Aim
To receive command messages from an MQTT broker and use them to actuate physical hardware (an LED) on the Raspberry Pi.

## Learning Objectives
* Complete the Publish/Subscribe IoT loop by acting as a Subscriber.
* Link network events (callbacks) to hardware actions.
* Create a remotely controllable device over the internet.

## Components Required
* Raspberry Pi (with Internet connection)
* LED
* 330Ω Resistor
* Breadboard & Jumper Wires

## Circuit Diagram / Hardware Connections

| Component | Raspberry Pi Pin |
| --------- | ---------------- |
| LED Anode (+)| GPIO 17 (Pin 11)|
| LED Cathode (-)| GND (Pin 6) via 330Ω Resistor|

*Note: All GPIO references use BCM numbering.*

## Software Requirements
```bash
pip install paho-mqtt nielit-rpi
```

## How It Works
This script connects to the MQTT broker and subscribes to the topic `nielit/rpi/led`. The script then enters an infinite loop (`loop_forever()`), waiting in the background. Whenever a message is published to that topic by *any* device in the world, the broker forwards it to the Raspberry Pi. The `message_handler` callback function is triggered, which parses the message payload. If the payload says "on", it turns the physical LED on; if "off", it turns the LED off.

## Running the Program
Execute the script:
```bash
python main.py
```
To test this, you need a way to publish messages. You can use an MQTT client on your phone (like MQTT Dash), a desktop app (like MQTTX), or another terminal window using Mosquitto CLI:
```bash
mosquitto_pub -h test.mosquitto.org -t "nielit/rpi/led" -m "on"
mosquitto_pub -h test.mosquitto.org -t "nielit/rpi/led" -m "off"
```

## Expected Output
**Terminal:**
```
Starting MQTT Subscriber Practical...
Broker: test.mosquitto.org:1883
Topic: nielit/rpi/led
Connecting to broker...
Listening for messages ('on' or 'off'). Press Ctrl+C to exit.
Received command: on
Received command: off
```

## Troubleshooting
* **Never receives messages**: Ensure the broker address and topic string match EXACTLY with the publisher. Topics are case-sensitive. Check your internet connection.
* **Messages delayed**: This can happen on public brokers if they are overloaded. Try using a different public broker (e.g., `broker.hivemq.com`).

## Safety Notes
* Since this uses a public unauthenticated topic, anyone who guesses the topic name can turn your LED on and off remotely. 
