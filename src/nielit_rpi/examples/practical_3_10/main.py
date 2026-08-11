"""
Practical 3_10: DHT11/DHT22 Temperature & Humidity.

This script reads temperature and humidity data from a DHT11 sensor
using the nielit_rpi library.
"""
import time
import sys
from nielit_rpi.sensors import DHTSensor

DHT_PIN: int = 4
POLL_INTERVAL_SEC: float = 2.0

def main() -> None:
    """Main loop to continuously read and display sensor data."""
    print("DHT11 Temperature & Humidity Sensor.")
    print(f"Reading from GPIO {DHT_PIN}. Press Ctrl+C to stop.")
    
    # Initialize the DHT sensor (assumes DHT11 by default, or configurable via the class)
    sensor = DHTSensor(pin=DHT_PIN, sensor_type="DHT11")
    
    try:
        while True:
            try:
                temperature = sensor.get_temperature()
                humidity = sensor.get_humidity()
                
                print(f"Temperature: {temperature:.1f} C | Humidity: {humidity:.1f} %")
            except Exception as e:
                # DHT sensors are prone to occasional read errors
                print(f"Sensor retry: {e}", file=sys.stderr)
            
            time.sleep(POLL_INTERVAL_SEC)
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        sensor.close()

if __name__ == "__main__":
    main()
