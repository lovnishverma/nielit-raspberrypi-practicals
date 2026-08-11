# Practical 3_10 — DHT11/DHT22 Temperature & Humidity

## Aim
To read temperature and relative humidity data from a digital DHT sensor.

## Learning Objectives
* Interface a one-wire digital sensor with the Raspberry Pi.
* Handle intermittent hardware read failures gracefully using try/except blocks.
* Process and format sensory data output.

## Components Required
* Raspberry Pi
* 1x DHT11 or DHT22 Sensor
* 1x 10kΩ Pull-up Resistor (if not built into the sensor module)
* Breadboard and Jumper wires

## Circuit Diagram / Hardware Connections
* Sensor VCC -> 3.3V or 5V Pin (check your specific module)
* Sensor GND -> GND
* Sensor DATA -> GPIO 4
* *If using a bare sensor component, place a 10kΩ resistor between VCC and DATA.*

## Software Requirements
* `nielit_rpi` library
* (Under the hood, this relies on libraries like `adafruit-circuitpython-dht` and `libgpiod2`)

## How It Works
The DHT11 utilizes a proprietary single-wire protocol to transmit data. Reading it requires precise microsecond timing, which can sometimes be interrupted by the Raspberry Pi's Linux OS scheduling. Because of this, it is standard practice to wrap the read commands in a `try...except` block, retrying on failure. The `DHTSensor` class abstracts the lower-level adafruit module initialization.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
DHT11 Temperature & Humidity Sensor.
Reading from GPIO 4. Press Ctrl+C to stop.
Temperature: 24.5 C | Humidity: 55.0 %
Temperature: 24.5 C | Humidity: 55.0 %
Sensor retry: Checksum did not validate. Try again.
Temperature: 24.6 C | Humidity: 55.0 %
```

## Troubleshooting
* **Frequent "Sensor retry" errors**: This is normal due to OS timing interruptions. If it *never* succeeds, check your wiring and ensure you have a pull-up resistor if required.
* **Module not found error for adafruit**: Make sure you have installed the necessary dependencies (`libgpiod2` via apt, and the correct pip modules).
* **Inaccurate readings**: DHT11 sensors have a margin of error of ±2°C and ±5% humidity. Ensure the sensor is not placed near a heat source.

## Safety Notes
* Double-check the pinout for your specific DHT module, as some pre-mounted modules swap the DATA and GND pins compared to the bare component.

## GPIO Reference
* All practicals use BCM numbering.
