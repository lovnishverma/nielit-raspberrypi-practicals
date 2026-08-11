"""
Practical 3.12: PIR Motion Detection

This practical demonstrates how to read a PIR motion sensor.
"""
from signal import pause
from nielit_rpi.sensors import PIRSensor

# Named constant for GPIO pin
PIR_PIN = 4

def motion_detected() -> None:
    """Callback for when motion is detected."""
    print("Motion detected!")

def no_motion() -> None:
    """Callback for when motion stops."""
    print("No motion.")

def main() -> None:
    """Main execution function."""
    print("Starting PIR Motion Detection Practical...")
    print(f"Monitoring GPIO {PIR_PIN} for motion...")
    
    pir = None
    try:
        pir = PIRSensor(pin=PIR_PIN)
        pir.when_motion = motion_detected
        pir.when_no_motion = no_motion
        
        print("Press Ctrl+C to exit.")
        pause()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    finally:
        print("Cleaning up GPIO resources...")
        if pir:
            pir.close()
        print("Done.")

if __name__ == "__main__":
    main()
