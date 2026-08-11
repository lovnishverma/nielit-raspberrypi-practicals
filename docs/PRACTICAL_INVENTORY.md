# Practical Inventory

| Practical Number | Title | Description | Main Components | GPIO Pins | Communication Protocol | Python Dependencies | External Services | Entry Point | Original File(s) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 3_1 | System Information | RPi system info display | No hardware | No GPIO | None | platform,shutil (stdlib) | None | examples/practical_3_1/main.py | examples/practical_3_1/main.py |
| 3_2 | GPIO LED Output | Blink LED | LED+resistor | GPIO 17 | Digital OUT | gpiozero | None | examples/practical_3_2/main.py | examples/practical_3_2/main.py |
| 3_3 | Push Button Input | Read button state | Button | GPIO 27 | Digital IN | gpiozero | None | examples/practical_3_3/main.py | examples/practical_3_3/main.py |
| 3_4 | Button Controlled LED | Button controls LED | Button+LED | GPIO 17,27 | Digital IN/OUT | gpiozero | None | - | - |
| 3_5 | Traffic Light Controller | 3-LED traffic sequence | 3 LEDs+resistors | GPIO 17,27,22 | Digital OUT | gpiozero | None | - | - |
| 3_6 | PWM LED Brightness | Fade LED with PWM | LED+resistor | GPIO 18 | PWM | gpiozero | None | - | - |
| 3_7 | Buzzer Alert | Sound buzzer pattern | Active buzzer | GPIO 23 | Digital OUT | gpiozero | None | - | - |
| 3_8 | Servo Motor Control | Control servo angles | SG90 servo | GPIO 18 | PWM | gpiozero | None | - | - |
| 3_9 | HC-SR04 Distance Measurement | Measure distance | HC-SR04 | GPIO 23,24 | Digital IN/OUT | gpiozero | None | - | - |
| 3_10 | DHT11 Temperature & Humidity | Read temp/humidity | DHT11 | GPIO 4 (board.D4) | OneWire | adafruit-circuitpython-dht,board | None | - | - |
| 3_11 | I2C LCD Display | Show text on LCD | 16x2 I2C LCD | SDA(GPIO 2),SCL(GPIO 3) | I2C | smbus2 | None | - | - |
| 3_12 | PIR Motion Detection | Detect motion | PIR sensor | GPIO 4 | Digital IN | gpiozero | None | - | - |
| 3_13 | Relay Control | Switch relay | Relay module | GPIO 17 | Digital OUT | gpiozero | None | - | - |
| 3_14 | LDR + MCP3008 ADC | Read light level | MCP3008+LDR | SPI (CH0) | SPI | gpiozero | None | - | - |
| 3_15 | MFRC522 RFID | Read RFID card | MFRC522+tag | SPI | SPI | mfrc522 | None | - | - |
| 3_16 | SQLite Sensor Logger | Log sensor data | RPi only | None | SQLite | sqlite3 (stdlib) | None | - | - |
| 3_17 | Flask GPIO Web Control | Web LED control | LED+LAN | GPIO 17 | HTTP | flask,gpiozero | None | - | - |
| 3_18 | MQTT Publisher | Publish MQTT msgs | Network | None | MQTT | paho-mqtt | MQTT broker | - | - |
| 3_19 | MQTT Subscriber + GPIO | Subscribe & control LED | LED+MQTT | GPIO 17 | MQTT | paho-mqtt,gpiozero | MQTT broker | - | - |
| 3_20 | Smart Home Capstone | Auto lighting | PIR+LED | GPIO 4,17 | Digital IN/OUT | gpiozero | None | - | - |
