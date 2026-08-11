"""
Practical 3_9: HC-SR04 Distance Measurement.

This script measures distance using an HC-SR04 Ultrasonic Sensor
via the nielit_rpi library.
"""
import time
from nielit_rpi.sensors import UltrasonicSensor

TRIGGER_PIN: int = 23
ECHO_PIN: int = 24
POLL_INTERVAL_SEC: float = 0.5

def main() -> None:
    """Main loop to continuously measure distance."""
    print("Ultrasonic Distance Measurement.")
    print(f"Trigger: GPIO {TRIGGER_PIN}, Echo: GPIO {ECHO_PIN}")
    print("Press Ctrl+C to stop.")
    
    sensor = UltrasonicSensor(trigger_pin=TRIGGER_PIN, echo_pin=ECHO_PIN, max_distance=4.0)
    
    try:
        while True:
            # Assume get_distance() returns distance in meters
            distance_m = sensor.get_distance()
            distance_cm = distance_m * 100
            print(f"Distance: {distance_cm:.1f} cm", end="\r", flush=True)
            time.sleep(POLL_INTERVAL_SEC)
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        sensor.close()

if __name__ == "__main__":
    main()
