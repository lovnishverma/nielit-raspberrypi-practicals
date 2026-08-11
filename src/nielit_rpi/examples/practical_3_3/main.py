"""
Practical 3_3: Push Button Input.

This script reads the state of a push button connected to a GPIO pin
using the nielit_rpi library and prints whether it is pressed or released.
"""
import time
from nielit_rpi.gpio import ButtonReader

BUTTON_PIN: int = 27
POLL_INTERVAL_SEC: float = 0.1

def main() -> None:
    """Main loop to monitor button state."""
    print(f"Monitoring Button on GPIO {BUTTON_PIN}. Press Ctrl+C to stop.")
    button = ButtonReader(pin=BUTTON_PIN, pull_up=True)
    try:
        while True:
            state: str = "PRESSED" if button.is_pressed() else "RELEASED"
            print(f"Button State: {state}    ", end="\r", flush=True)
            time.sleep(POLL_INTERVAL_SEC)
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        button.close()

if __name__ == "__main__":
    main()
