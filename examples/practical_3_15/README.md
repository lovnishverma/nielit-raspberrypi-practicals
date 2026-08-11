# Practical 3_15 — MFRC522 RFID

## Aim
To interface an MFRC522 RFID reader with the Raspberry Pi and read data from MIFARE RFID tags.

## Learning Objectives
* Understand Radio Frequency Identification (RFID) technology.
* Learn how to use SPI for communication with complex sensor modules.
* Read unique IDs and data from contactless tags.

## Components Required
* Raspberry Pi
* RC522 RFID Reader Module
* MIFARE Classic 1K RFID Tags/Cards
* Jumper Wires (Female-to-Female)

## Circuit Diagram / Hardware Connections

| RC522 Pin | Raspberry Pi Pin |
| --------- | ---------------- |
| 3.3V      | 3.3V (Pin 1 or 17)|
| RST       | GPIO 25 (Pin 22) |
| GND       | GND (Pin 6)      |
| MISO      | MISO / GPIO 9 (Pin 21) |
| MOSI      | MOSI / GPIO 10 (Pin 19)|
| SCK       | SCLK / GPIO 11 (Pin 23)|
| SDA (CS)  | CE0 / GPIO 8 (Pin 24)  |

*Note: All GPIO references use BCM numbering.*

## Software Requirements
Ensure SPI is enabled on your Raspberry Pi (via `sudo raspi-config`).
```bash
pip install mfrc522 nielit-rpi
```

## How It Works
The MFRC522 module uses a 13.56 MHz electromagnetic field to communicate with passive RFID tags. When a tag enters the field, it powers up and transmits its unique identification number (UID) and any stored memory blocks. The reader communicates this data back to the Raspberry Pi over the SPI bus. The `RFIDReader` class (wrapping `SimpleMFRC522`) abstracts the complex register configuration required to negotiate with the card, providing a simple `read()` function that blocks until a card is detected.

## Running the Program
Execute the script:
```bash
python main.py
```

## Expected Output
**Terminal:**
```
Starting MFRC522 RFID Practical...
Place an RFID card/tag near the reader.
Card ID: 419385610293
Stored Text: 
Cleaning up GPIO resources...
Done.
```

## Troubleshooting
* **Module not reading anything**: Ensure the SPI connections are solid and correct. Swap MOSI and MISO if unsure, as they are often confused.
* **SPI error**: Check that SPI is enabled in `raspi-config`.
* **Inconsistent reads**: Keep the RC522 module away from metal surfaces, as they can interfere with the electromagnetic field.

## Safety Notes
* **3.3V Power Only**: The RC522 module is strict about 3.3V. Connecting it to 5V will permanently destroy the chip.
