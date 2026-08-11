import logging
from typing import Optional
from gpiozero import Buzzer

logger = logging.getLogger(__name__)

class BuzzerController:
    """
    A controller for an active buzzer connected to a GPIO pin.
    
    This class wraps gpiozero.Buzzer for simple sound generation.
    """
    
    def __init__(self, pin: int):
        """
        Initialize the Buzzer controller.
        
        Args:
            pin (int): BCM GPIO pin number.
        """
        logger.info(f"Initializing Buzzer on pin {pin}")
        self._buzzer = Buzzer(pin)
        
    def on(self) -> None:
        """Turn the buzzer on."""
        logger.info(f"Turning ON buzzer on pin {self._buzzer.pin.number}")
        self._buzzer.on()
        
    def off(self) -> None:
        """Turn the buzzer off."""
        logger.info(f"Turning OFF buzzer on pin {self._buzzer.pin.number}")
        self._buzzer.off()
        
    def beep(self, on_time: float = 1.0, off_time: float = 1.0, n: Optional[int] = None) -> None:
        """
        Beep the buzzer.
        
        Args:
            on_time (float): Number of seconds on.
            off_time (float): Number of seconds off.
            n (int, optional): Number of times to beep (None means forever).
        """
        logger.info(f"Beeping buzzer on pin {self._buzzer.pin.number} (on={on_time}s, off={off_time}s, n={n})")
        self._buzzer.beep(on_time=on_time, off_time=off_time, n=n)
        
    def close(self) -> None:
        """Close the buzzer connection and release resources."""
        if hasattr(self, '_buzzer') and self._buzzer:
            logger.info(f"Closing Buzzer on pin {self._buzzer.pin.number}")
            self._buzzer.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
