"""
Practical 3.13: Relay Control

This practical demonstrates how to safely switch a relay module.
"""
import time
from nielit_rpi.actuators import RelayController

# Named constant for GPIO pin
RELAY_PIN = 17

def main() -> None:
    """Main execution function."""
    print("Starting Relay Control Practical...")
    relay = None
    try:
        # Initialize the relay controller on GPIO 17
        relay = RelayController(pin=RELAY_PIN, active_high=True, initial_value=False)
        
        print("Turning relay ON...")
        relay.on()
        time.sleep(3)
        
        print("Turning relay OFF...")
        relay.off()
        time.sleep(1)
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    finally:
        print("Cleaning up GPIO resources...")
        if relay:
            relay.off()
            relay.close()
        print("Done.")

if __name__ == "__main__":
    main()
