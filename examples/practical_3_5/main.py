"""
Practical 3_5: Traffic Light Controller.

This script simulates a traffic light sequence using three LEDs
(Red, Yellow, Green) connected to GPIO pins.
"""
import time
from nielit_rpi.gpio import LEDController

RED_PIN: int = 17
YELLOW_PIN: int = 27
GREEN_PIN: int = 22

RED_DELAY: float = 5.0
GREEN_DELAY: float = 5.0
YELLOW_DELAY: float = 2.0

def main() -> None:
    """Main loop for the traffic light sequence."""
    print("Starting Traffic Light Controller. Press Ctrl+C to stop.")
    red = LEDController(pin=RED_PIN)
    yellow = LEDController(pin=YELLOW_PIN)
    green = LEDController(pin=GREEN_PIN)

    try:
        while True:
            # Red Light
            red.on()
            time.sleep(RED_DELAY)
            red.off()

            # Green Light
            green.on()
            time.sleep(GREEN_DELAY)
            green.off()

            # Yellow Light
            yellow.on()
            time.sleep(YELLOW_DELAY)
            yellow.off()
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        red.close()
        yellow.close()
        green.close()

if __name__ == "__main__":
    main()
