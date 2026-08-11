# Practical 3_16 — SQLite Sensor Logger

## Aim
To log sensor data locally on the Raspberry Pi using an SQLite database.

## Learning Objectives
* Understand persistent data storage concepts for IoT devices.
* Learn basic SQL commands (CREATE TABLE, INSERT).
* Manage database connections efficiently in Python.

## Components Required
* Raspberry Pi
* (Optional) Any temperature sensor like DHT11 or DS18B20. *This practical uses a software simulation.*

## Circuit Diagram / Hardware Connections
No specific hardware required for this practical, as it focuses on software data storage and uses a simulated temperature reading.

## Software Requirements
```bash
pip install nielit-rpi
```

## How It Works
IoT devices often need to store data locally if network connectivity drops, or for long-term historical analysis. SQLite is a lightweight, file-based relational database that requires no separate server process. The code establishes a single connection to `sensor_data.db` using `nielit_rpi.storage.SensorDataLogger`, creates a table to hold the data, and loops multiple times to simulate reading a sensor. The timestamp and sensor value are inserted into the database and committed. Using a single connection for the loop is significantly more efficient than opening and closing the database file for every reading.

## Running the Program
Execute the script:
```bash
python main.py
```
To verify the data was saved, you can inspect the database file using the sqlite3 command line:
```bash
sqlite3 sensor_data.db "SELECT * FROM readings;"
```

## Expected Output
**Terminal:**
```
Starting SQLite Sensor Logger Practical...
Database 'sensor_data.db' initialized. Logging 10 readings...
Logged [1/10] - Time: 2023-10-25T14:30:00, Temp: 25.00°C
Logged [2/10] - Time: 2023-10-25T14:30:02, Temp: 25.10°C
...
Successfully saved 10 readings to 'sensor_data.db'.
Closing database connection...
Done.
```

## Troubleshooting
* **Database Locked Error**: This happens if multiple scripts try to write to the SQLite database simultaneously, or if a previous run crashed without closing the connection. Ensure the database connection is cleanly closed in the `finally` block.
* **Permission Denied**: Ensure you have write permissions in the directory where the script is running, as it needs to create the `.db` file.

## Safety Notes
* Continuous rapid writing to an SD card can degrade its lifespan. In production IoT systems logging high-frequency data, consider writing to a RAM disk (tmpfs) and periodically syncing to the SD card, or use an external SSD/USB drive.
