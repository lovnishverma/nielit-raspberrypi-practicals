"""
Practical 3_6: PWM LED Brightness.

This script demonstrates fading an LED in and out using Pulse Width Modulation (PWM)
via the nielit_rpi library.
"""
import time
from nielit_rpi.gpio import PWMLEDController

PWM_PIN: int = 18
FADE_STEPS: int = 20
FADE_DELAY: float = 0.05
ITERATIONS: int = 3

def main() -> None:
    """Main loop to fade the LED in and out."""
    print(f"Fading LED on GPIO {PWM_PIN} using PWM. Running {ITERATIONS} cycles.")
    led = PWMLEDController(pin=PWM_PIN)
    
    try:
        for cycle in range(ITERATIONS):
            print(f"Cycle {cycle + 1}/{ITERATIONS}")
            # Fade in
            for i in range(FADE_STEPS + 1):
                led.set_value(i / FADE_STEPS)
                time.sleep(FADE_DELAY)
            
            # Fade out
            for i in range(FADE_STEPS, -1, -1):
                led.set_value(i / FADE_STEPS)
                time.sleep(FADE_DELAY)
    except KeyboardInterrupt:
        print("\nExiting program prematurely.")
    finally:
        led.close()

if __name__ == "__main__":
    main()
