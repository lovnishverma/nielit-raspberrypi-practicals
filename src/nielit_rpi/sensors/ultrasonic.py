import logging
from gpiozero import DistanceSensor

logger = logging.getLogger(__name__)

class UltrasonicSensor:
    """
    A controller for an HC-SR04 ultrasonic distance sensor.
    
    Wraps gpiozero.DistanceSensor.
    """
    
    def __init__(self, trigger_pin: int, echo_pin: int, max_distance: float = 4.0):
        """
        Initialize the Ultrasonic sensor.
        
        Args:
            trigger_pin (int): BCM GPIO pin for TRIGGER.
            echo_pin (int): BCM GPIO pin for ECHO.
            max_distance (float): Maximum distance in meters to measure.
        """
        logger.info(f"Initializing Ultrasonic Sensor (Trigger={trigger_pin}, Echo={echo_pin})")
        self._sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=max_distance)
        
    @property
    def distance_m(self) -> float:
        """Get distance in meters."""
        return self._sensor.distance
        
    @property
    def distance_cm(self) -> float:
        """Get distance in centimeters."""
        return self._sensor.distance * 100.0
        
    def in_range(self, threshold_cm: float) -> bool:
        """
        Check if an object is within a given threshold.
        
        Args:
            threshold_cm (float): Threshold in centimeters.
            
        Returns:
            bool: True if object is closer than threshold, False otherwise.
        """
        return self.distance_cm <= threshold_cm
        
    def close(self) -> None:
        """Close the sensor and release resources."""
        if hasattr(self, '_sensor') and self._sensor:
            logger.info("Closing Ultrasonic Sensor")
            self._sensor.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
