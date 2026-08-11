import logging
from typing import Optional
from gpiozero import LED

logger = logging.getLogger(__name__)

class LEDController:
    """
    A controller for an LED connected to a GPIO pin.
    
    This class wraps gpiozero.LED to provide educational context and logging.
    A GPIO (General Purpose Input/Output) output pin can be set to HIGH (on)
    or LOW (off). Connecting an LED with a suitable resistor allows you to
    see the state of the pin visually.
    """
    
    def __init__(self, pin: int):
        """
        Initialize the LED controller.
        
        Args:
            pin (int): BCM GPIO pin number the LED is connected to.
        """
        logger.info(f"Initializing LED on pin {pin}")
        self._led = LED(pin)
        
    def on(self) -> None:
        """Turn the LED on."""
        logger.info(f"Turning ON LED on pin {self._led.pin.number}")
        self._led.on()
        
    def off(self) -> None:
        """Turn the LED off."""
        logger.info(f"Turning OFF LED on pin {self._led.pin.number}")
        self._led.off()
        
    def toggle(self) -> None:
        """Toggle the LED state."""
        logger.info(f"Toggling LED on pin {self._led.pin.number}")
        self._led.toggle()
        
    def blink(self, on_time: float = 1.0, off_time: float = 1.0, n: Optional[int] = None) -> None:
        """
        Blink the LED.
        
        Args:
            on_time (float): Number of seconds on.
            off_time (float): Number of seconds off.
            n (int, optional): Number of times to blink (None means forever).
        """
        logger.info(f"Blinking LED on pin {self._led.pin.number} (on={on_time}s, off={off_time}s, n={n})")
        self._led.blink(on_time=on_time, off_time=off_time, n=n)
        
    @property
    def is_lit(self) -> bool:
        """Return True if the LED is currently on."""
        return self._led.is_lit
        
    def close(self) -> None:
        """Close the LED connection and release resources."""
        if hasattr(self, '_led') and self._led:
            logger.info(f"Closing LED on pin {self._led.pin.number}")
            self._led.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
