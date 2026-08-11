"""
Practical 3_7: Buzzer Alert.

This script demonstrates controlling an active buzzer to create
audible alerts using the nielit_rpi library.
"""
import time
from nielit_rpi.gpio import BuzzerController

BUZZER_PIN: int = 23
ITERATIONS: int = 5
BEEP_DURATION: float = 0.2
PAUSE_DURATION: float = 0.2

def main() -> None:
    """Main loop to sound the buzzer."""
    print(f"Sounding buzzer on GPIO {BUZZER_PIN} for {ITERATIONS} beeps.")
    buzzer = BuzzerController(pin=BUZZER_PIN)
    
    try:
        for i in range(ITERATIONS):
            buzzer.on()
            time.sleep(BEEP_DURATION)
            buzzer.off()
            time.sleep(PAUSE_DURATION)
    except KeyboardInterrupt:
        print("\nExiting program prematurely.")
    finally:
        buzzer.close()

if __name__ == "__main__":
    main()
