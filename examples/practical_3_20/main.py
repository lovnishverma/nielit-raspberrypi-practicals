"""
Practical 3.20: Smart Home Automation Capstone

This capstone integrates a PIR motion sensor, an ambient light sensor (simulated),
and an LED to create an automated smart lighting system.
"""
import time
from nielit_rpi.sensors import PIRSensor
from nielit_rpi.gpio import LEDController

# Configuration
PIR_PIN = 4
LED_PIN = 17
LIGHT_THRESHOLD = 0.35
LOOP_DELAY = 0.2

def read_ambient_level() -> float:
    """
    Stub for reading ambient light level.
    In a full hardware version, this would use MCP3008 + LDR 
    as demonstrated in Practical 3.14.
    Returns a normalized float (0.0 = dark, 1.0 = bright).
    """
    # Hardcoded to simulate a dark room for demonstration purposes
    return 0.2 

def main() -> None:
    """Main execution function."""
    print("Starting Smart Home Automation Capstone...")
    
    pir = None
    light = None
    try:
        # Initialize hardware
        pir = PIRSensor(pin=PIR_PIN)
        light = LEDController(pin=LED_PIN)
        
        print("System Active: Monitoring motion and ambient light...")
        print("Press Ctrl+C to exit.")
        
        while True:
            motion = pir.motion_detected
            ambient = read_ambient_level()
            
            # Logic: Turn on light ONLY if motion is detected AND it is dark
            if motion and ambient < LIGHT_THRESHOLD:
                if not light.is_lit:
                    print("Motion detected in dark area. Turning light ON.")
                    light.on()
            else:
                if light.is_lit:
                    print("No motion or sufficient ambient light. Turning light OFF.")
                    light.off()
                    
            time.sleep(LOOP_DELAY)
            
    except KeyboardInterrupt:
        print("\nSystem deactivated by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Cleaning up hardware resources...")
        if light:
            light.off()
            light.close()
        if pir:
            pir.close()
        print("Done.")

if __name__ == "__main__":
    main()
