"""
Practical 3.11: I2C LCD Display

This practical demonstrates how to interface and display text on a 16x2 I2C LCD.
"""
import time
from nielit_rpi.displays import I2CLCD

def main() -> None:
    """Main execution function."""
    print("Starting I2C LCD Display Practical...")
    lcd = None
    try:
        # Initialize the LCD at address 0x27 on I2C bus 1
        lcd = I2CLCD(address=0x27, bus=1)
        print("LCD Initialized.")
        
        lcd.clear()
        lcd.display_string("NIELIT Raspberry", line=1)
        lcd.display_string("I2C LCD Practical", line=2)
        
        print("Text displayed. Keep running for 5 seconds.")
        time.sleep(5)
        
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        print("Cleaning up...")
        if lcd:
            try:
                lcd.clear()
            except Exception:
                pass
        print("Done.")

if __name__ == "__main__":
    main()
