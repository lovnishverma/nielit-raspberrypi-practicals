"""
Practical 3.19: MQTT Subscriber + GPIO

This practical demonstrates receiving commands over MQTT to control a local LED.
"""
import os
from nielit_rpi.communication import MQTTSubscriber
from nielit_rpi.gpio import LEDController

# Configuration
BROKER = os.getenv("MQTT_BROKER", "test.mosquitto.org")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = os.getenv("MQTT_TOPIC", "nielit/rpi/led")
LED_PIN = 17

# Global hardware controller
led = None

def message_handler(payload: str) -> None:
    """Callback function executed when a message arrives."""
    cmd = payload.strip().lower()
    print(f"Received command: {cmd}")
    
    if led:
        if cmd == "on":
            led.on()
        elif cmd == "off":
            led.off()
        else:
            print(f"Unknown command: {cmd}")

def main() -> None:
    """Main execution function."""
    global led
    print("Starting MQTT Subscriber Practical...")
    print(f"Broker: {BROKER}:{PORT}")
    print(f"Topic: {TOPIC}")
    
    subscriber = None
    try:
        # Initialize hardware
        led = LEDController(pin=LED_PIN)
        
        # Initialize MQTT subscriber
        subscriber = MQTTSubscriber(broker=BROKER, port=PORT, topic=TOPIC)
        subscriber.on_message_received = message_handler
        
        print("Connecting to broker...")
        subscriber.connect()
        
        print("Listening for messages ('on' or 'off'). Press Ctrl+C to exit.")
        # Block and process network traffic indefinitely
        subscriber.loop_forever()
        
    except KeyboardInterrupt:
        print("\nSubscriber stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Cleaning up resources...")
        if subscriber:
            subscriber.disconnect()
        if led:
            led.off()
            led.close()
        print("Done.")

if __name__ == "__main__":
    main()
