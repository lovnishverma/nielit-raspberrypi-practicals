import logging
from typing import Optional, Callable
from gpiozero import Button

logger = logging.getLogger(__name__)

class ButtonReader:
    """
    A reader for a push button connected to a GPIO pin.
    
    This class wraps gpiozero.Button to provide logging and ease of use.
    It reads digital inputs from a switch.
    """
    
    def __init__(self, pin: int, pull_up: bool = True, bounce_time: Optional[float] = None):
        """
        Initialize the Button reader.
        
        Args:
            pin (int): BCM GPIO pin number.
            pull_up (bool): If True, pull up resistor is active (default).
            bounce_time (float, optional): Software switch bounce time in seconds.
        """
        logger.info(f"Initializing Button on pin {pin} (pull_up={pull_up})")
        self._button = Button(pin, pull_up=pull_up, bounce_time=bounce_time)
        
    @property
    def is_pressed(self) -> bool:
        """Return True if the button is pressed."""
        return self._button.is_pressed
        
    def wait_for_press(self, timeout: Optional[float] = None) -> bool:
        """Wait until the button is pressed."""
        logger.info(f"Waiting for button press on pin {self._button.pin.number} (timeout={timeout})")
        return self._button.wait_for_press(timeout=timeout)
        
    def wait_for_release(self, timeout: Optional[float] = None) -> bool:
        """Wait until the button is released."""
        logger.info(f"Waiting for button release on pin {self._button.pin.number} (timeout={timeout})")
        return self._button.wait_for_release(timeout=timeout)
        
    @property
    def when_pressed(self) -> Optional[Callable]:
        return self._button.when_pressed
        
    @when_pressed.setter
    def when_pressed(self, callback: Optional[Callable]):
        logger.info(f"Setting when_pressed callback for button on pin {self._button.pin.number}")
        self._button.when_pressed = callback
        
    @property
    def when_released(self) -> Optional[Callable]:
        return self._button.when_released
        
    @when_released.setter
    def when_released(self, callback: Optional[Callable]):
        logger.info(f"Setting when_released callback for button on pin {self._button.pin.number}")
        self._button.when_released = callback
        
    def close(self) -> None:
        """Close the button connection and release resources."""
        if hasattr(self, '_button') and self._button:
            logger.info(f"Closing Button on pin {self._button.pin.number}")
            self._button.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
