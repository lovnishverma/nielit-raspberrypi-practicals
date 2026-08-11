# Practical 3_14 — LDR + MCP3008 ADC

## Aim
To read analog sensor data (from a Light Dependent Resistor) into the Raspberry Pi using an MCP3008 Analog-to-Digital Converter (ADC).

## Learning Objectives
* Understand the difference between analog and digital signals.
* Learn how to use the SPI (Serial Peripheral Interface) protocol.
* Read analog voltage variations caused by a voltage divider circuit.

## Components Required
* Raspberry Pi
* MCP3008 ADC Chip
* LDR (Light Dependent Resistor / Photoresistor)
* 10kΩ Resistor
* Breadboard & Jumper Wires

## Circuit Diagram / Hardware Connections

**MCP3008 to Raspberry Pi (SPI):**
| MCP3008 Pin | Raspberry Pi Pin |
| ----------- | ---------------- |
| VDD (16)    | 3.3V (Pin 1 or 17)|
| VREF (15)   | 3.3V             |
| AGND (14)   | GND (Pin 39 or other)|
| CLK (13)    | SCLK / GPIO 11 (Pin 23)|
| DOUT (12)   | MISO / GPIO 9 (Pin 21) |
| DIN (11)    | MOSI / GPIO 10 (Pin 19)|
| CS (10)     | CE0 / GPIO 8 (Pin 24)  |
| DGND (9)    | GND              |

**LDR Voltage Divider to MCP3008:**
* Connect one leg of the LDR to **3.3V**.
* Connect the other leg of the LDR to **MCP3008 CH0 (Pin 1)**.
* Connect a **10kΩ resistor** from **MCP3008 CH0 (Pin 1)** to **GND**.

*Note: All GPIO references use BCM numbering.*

## Software Requirements
Ensure SPI is enabled on your Raspberry Pi (via `sudo raspi-config`).
```bash
pip install nielit-rpi
```

## How It Works
The Raspberry Pi has no built-in analog inputs. The MCP3008 is an 8-channel, 10-bit Analog-to-Digital Converter that communicates over the SPI bus. The LDR and the 10kΩ resistor form a voltage divider. As light intensity changes, the LDR's resistance changes, which alters the voltage at CH0. The MCP3008 converts this analog voltage (0V to 3.3V) into a digital value (0 to 1023). The `nielit_rpi.sensors.LDRSensor` scales this to a normalized value between 0.0 and 1.0.

## Running the Program
Execute the script:
```bash
python main.py
```

## Expected Output
**Terminal:**
```
Starting LDR + MCP3008 ADC Practical...
Reading light levels. Press Ctrl+C to exit.
LDR Value: 0.452 | Voltage: 1.492 V
LDR Value: 0.455 | Voltage: 1.502 V
LDR Value: 0.890 | Voltage: 2.937 V  <-- (Bright light shone on sensor)
LDR Value: 0.120 | Voltage: 0.396 V  <-- (Sensor covered by hand)
```

## Troubleshooting
* **Always reads 0.0 or 1.0**: Check your wiring carefully, especially the SPI connections (MOSI/MISO/CLK) and ensure the voltage divider is correct.
* **Permission Denied / SPI errors**: Verify that the SPI interface is enabled in `raspi-config`.

## Safety Notes
* Double-check connections to the MCP3008. Incorrectly wiring the VDD/VREF pins to 5V while connecting SPI to the Pi can damage the Pi's 3.3V logic pins.
