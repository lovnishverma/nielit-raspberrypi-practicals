import logging
from typing import Optional, Callable
from gpiozero import MotionSensor

logger = logging.getLogger(__name__)

class PIRSensor:
    """
    A controller for a Passive Infrared (PIR) Motion Sensor.
    
    Wraps gpiozero.MotionSensor.
    """
    
    def __init__(self, pin: int, queue_len: int = 1, sample_rate: float = 10, threshold: float = 0.5):
        """
        Initialize the PIR sensor.
        
        Args:
            pin (int): BCM GPIO pin number.
            queue_len (int): Length of the queue used to store values.
            sample_rate (float): Number of values to read per second.
            threshold (float): Threshold to consider motion detected.
        """
        logger.info(f"Initializing PIR Sensor on pin {pin}")
        self._sensor = MotionSensor(
            pin, 
            queue_len=queue_len, 
            sample_rate=sample_rate, 
            threshold=threshold
        )
        
    @property
    def motion_detected(self) -> bool:
        """Return True if motion is currently detected."""
        return self._sensor.motion_detected
        
    @property
    def when_motion(self) -> Optional[Callable]:
        return self._sensor.when_motion
        
    @when_motion.setter
    def when_motion(self, callback: Optional[Callable]):
        logger.info(f"Setting when_motion callback for PIR sensor on pin {self._sensor.pin.number}")
        self._sensor.when_motion = callback
        
    @property
    def when_no_motion(self) -> Optional[Callable]:
        return self._sensor.when_no_motion
        
    @when_no_motion.setter
    def when_no_motion(self, callback: Optional[Callable]):
        logger.info(f"Setting when_no_motion callback for PIR sensor on pin {self._sensor.pin.number}")
        self._sensor.when_no_motion = callback
        
    def wait_for_motion(self, timeout: Optional[float] = None) -> bool:
        """Wait until motion is detected."""
        logger.info(f"Waiting for motion on PIR sensor (timeout={timeout})")
        return self._sensor.wait_for_motion(timeout=timeout)
        
    def wait_for_no_motion(self, timeout: Optional[float] = None) -> bool:
        """Wait until no motion is detected."""
        logger.info(f"Waiting for no motion on PIR sensor (timeout={timeout})")
        return self._sensor.wait_for_no_motion(timeout=timeout)
        
    def close(self) -> None:
        """Close the sensor and release resources."""
        if hasattr(self, '_sensor') and self._sensor:
            logger.info(f"Closing PIR Sensor on pin {self._sensor.pin.number}")
            self._sensor.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
