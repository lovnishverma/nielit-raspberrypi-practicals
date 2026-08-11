"""
Practical 3.18: MQTT Publisher

This practical demonstrates publishing simulated sensor data to an MQTT broker.
"""
import os
import time
import json
from nielit_rpi.communication import MQTTPublisher

# Configuration via environment variables with defaults
BROKER = os.getenv("MQTT_BROKER", "test.mosquitto.org")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = os.getenv("MQTT_TOPIC", "nielit/rpi/sensor")
DELAY = 2.0

def main() -> None:
    """Main execution function."""
    print("Starting MQTT Publisher Practical...")
    print(f"Broker: {BROKER}:{PORT}")
    print(f"Topic: {TOPIC}")
    
    publisher = None
    try:
        # Initialize the publisher
        publisher = MQTTPublisher(broker=BROKER, port=PORT)
        publisher.connect()
        
        print("Connected. Publishing messages...")
        for value in range(5):
            payload = {
                "device": "raspberry-pi",
                "value": value
            }
            # Convert dictionary to JSON string and publish
            msg = json.dumps(payload)
            publisher.publish(topic=TOPIC, payload=msg)
            
            print(f"Published: {msg}")
            time.sleep(DELAY)
            
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nPublisher interrupted by user.")
    finally:
        print("Disconnecting from broker...")
        if publisher:
            publisher.disconnect()
        print("Done.")

if __name__ == "__main__":
    main()
