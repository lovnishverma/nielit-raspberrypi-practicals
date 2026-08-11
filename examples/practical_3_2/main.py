"""
Practical 3_2: GPIO LED Output.

This script demonstrates blinking an LED connected to a GPIO pin
using the nielit_rpi library.
"""
import time
from nielit_rpi.gpio import LEDController

LED_PIN: int = 17
BLINK_INTERVAL_SEC: float = 1.0

def main() -> None:
    """Main loop to blink the LED."""
    print(f"Blinking LED on GPIO {LED_PIN}. Press Ctrl+C to stop.")
    led = LEDController(pin=LED_PIN)
    try:
        while True:
            led.on()
            time.sleep(BLINK_INTERVAL_SEC)
            led.off()
            time.sleep(BLINK_INTERVAL_SEC)
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        led.close()

if __name__ == "__main__":
    main()
