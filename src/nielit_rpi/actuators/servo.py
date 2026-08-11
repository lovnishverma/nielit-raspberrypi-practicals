import logging
import time
from gpiozero import AngularServo

logger = logging.getLogger(__name__)

class ServoController:
    """
    A controller for an RC hobby servo motor.
    
    WARNING: Servos draw significant current. Power them from a separate 5V supply 
    (with grounds connected), NOT directly from the Raspberry Pi 5V pin, to avoid 
    damaging your Pi or causing brownouts.
    
    Wraps gpiozero.AngularServo.
    """
    
    def __init__(self, pin: int, min_angle: float = -90, max_angle: float = 90, 
                 min_pulse_width: float = 0.0005, max_pulse_width: float = 0.0025):
        """
        Initialize the Servo controller.
        
        Args:
            pin (int): BCM GPIO pin number.
            min_angle (float): The minimum angle (e.g., -90).
            max_angle (float): The maximum angle (e.g., 90).
            min_pulse_width (float): Pulse width for min_angle (usually ~0.5ms).
            max_pulse_width (float): Pulse width for max_angle (usually ~2.5ms).
        """
        logger.info(f"Initializing Servo on pin {pin}")
        self._servo = AngularServo(
            pin, 
            min_angle=min_angle, 
            max_angle=max_angle,
            min_pulse_width=min_pulse_width, 
            max_pulse_width=max_pulse_width
        )
        
    @property
    def angle(self) -> float:
        """Get the current angle of the servo."""
        return self._servo.angle if self._servo.angle is not None else 0.0
        
    @angle.setter
    def angle(self, value: float) -> None:
        """Set the angle of the servo."""
        logger.debug(f"Setting servo on pin {self._servo.pin.number} to angle {value}")
        # Clamp value to min/max range
        safe_value = max(self._servo.min_angle, min(self._servo.max_angle, value))
        self._servo.angle = safe_value
        
    def min(self) -> None:
        """Set the servo to its minimum angle."""
        self._servo.min()
        
    def mid(self) -> None:
        """Set the servo to its middle position (0)."""
        self._servo.mid()
        
    def max(self) -> None:
        """Set the servo to its maximum angle."""
        self._servo.max()
        
    def sweep(self, step: float = 1.0, delay: float = 0.05) -> None:
        """
        Sweep the servo through its full range and back.
        
        Args:
            step (float): Angle increment step.
            delay (float): Delay in seconds between steps.
        """
        logger.info(f"Sweeping servo on pin {self._servo.pin.number}")
        # Forward sweep
        curr = self._servo.min_angle
        while curr <= self._servo.max_angle:
            self.angle = curr
            time.sleep(delay)
            curr += step
            
        # Backward sweep
        curr = self._servo.max_angle
        while curr >= self._servo.min_angle:
            self.angle = curr
            time.sleep(delay)
            curr -= step
            
    def detach(self) -> None:
        """Stop sending PWM pulses (let the servo go loose)."""
        logger.info(f"Detaching servo on pin {self._servo.pin.number}")
        self._servo.detach()
        
    def close(self) -> None:
        """Release resources used by the servo."""
        if hasattr(self, '_servo') and self._servo:
            logger.info(f"Closing Servo on pin {self._servo.pin.number}")
            self._servo.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
