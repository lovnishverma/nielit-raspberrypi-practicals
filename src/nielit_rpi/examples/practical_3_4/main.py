"""
Practical 3_4: Button Controlled LED.

This script demonstrates controlling an LED using a push button.
When the button is pressed, the LED turns on. When released, it turns off.
"""
import time
from nielit_rpi.gpio import LEDController, ButtonReader

LED_PIN: int = 17
BUTTON_PIN: int = 27
POLL_INTERVAL_SEC: float = 0.05

def main() -> None:
    """Setup components and poll button state to control LED."""
    print(f"Control LED (GPIO {LED_PIN}) with Button (GPIO {BUTTON_PIN}).")
    print("Press Ctrl+C to stop.")
    
    led = LEDController(pin=LED_PIN)
    button = ButtonReader(pin=BUTTON_PIN, pull_up=True)
    
    try:
        while True:
            if button.is_pressed():
                led.on()
            else:
                led.off()
            time.sleep(POLL_INTERVAL_SEC)
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        led.close()
        button.close()

if __name__ == "__main__":
    main()
