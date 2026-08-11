"""
Practical 3.16: SQLite Sensor Logger

This practical logs sensor data (simulated here) to a local SQLite database.
"""
import time
import sqlite3
from datetime import datetime
from nielit_rpi.storage import SensorDataLogger

# Configuration
DB_NAME = "sensor_data.db"
READINGS_COUNT = 10
DELAY = 2.0

def read_temperature() -> float:
    """Stub for reading a temperature sensor."""
    # In a real scenario, this would read from a DHT11/DS18B20/etc.
    return 25.0

def main() -> None:
    """Main execution function."""
    print("Starting SQLite Sensor Logger Practical...")
    
    # Initialize the database and table connection once
    logger = None
    try:
        logger = SensorDataLogger(db_path=DB_NAME)
        # Create table if it doesn't exist
        logger.execute_query(
            "CREATE TABLE IF NOT EXISTS readings("
            "id INTEGER PRIMARY KEY,"
            "timestamp TEXT,"
            "temperature REAL)"
        )
        print(f"Database '{DB_NAME}' initialized. Logging {READINGS_COUNT} readings...")
        
        for i in range(READINGS_COUNT):
            temp = read_temperature()
            # Adding slight variations to the simulated data for realism
            temp += (i * 0.1) 
            ts = datetime.now().isoformat(timespec="seconds")
            
            logger.execute_query(
                "INSERT INTO readings(timestamp, temperature) VALUES(?, ?)",
                (ts, temp)
            )
            
            print(f"Logged [{i+1}/{READINGS_COUNT}] - Time: {ts}, Temp: {temp:.2f}°C")
            time.sleep(DELAY)
            
        print(f"Successfully saved {READINGS_COUNT} readings to '{DB_NAME}'.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except KeyboardInterrupt:
        print("\nLogging interrupted by user.")
    finally:
        print("Closing database connection...")
        if logger:
            logger.close()
        print("Done.")

if __name__ == "__main__":
    main()
