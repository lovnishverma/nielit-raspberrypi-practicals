"""
Practical 3_8: Servo Motor Control.

This script demonstrates controlling an SG90 servo motor by sending it
to specific angles using the nielit_rpi library.
"""
import time
from nielit_rpi.actuators import ServoController

SERVO_PIN: int = 18
MOVE_DELAY: float = 1.0

# Define the sequence of angles
ANGLES: list[int] = [-90, -45, 0, 45, 90, 45, 0, -45, -90]

def main() -> None:
    """Main loop to move the servo to predefined angles."""
    print(f"Controlling Servo on GPIO {SERVO_PIN}.")
    print("Ensure the servo has an external 5V power supply.")
    
    # The default SG90 pulse widths are approximately 0.5ms to 2.5ms.
    # The nielit_rpi library abstractly manages the AngularServo setup.
    servo = ServoController(pin=SERVO_PIN, min_angle=-90, max_angle=90,
                            min_pulse_width=0.0005, max_pulse_width=0.0025)
    
    try:
        for angle in ANGLES:
            print(f"Moving to angle: {angle} degrees")
            servo.set_angle(angle)
            time.sleep(MOVE_DELAY)
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        servo.close()

if __name__ == "__main__":
    main()
