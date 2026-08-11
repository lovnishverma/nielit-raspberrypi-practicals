import logging
from typing import Optional
from gpiozero import PWMLED

logger = logging.getLogger(__name__)

class PWMLEDController:
    """
    A controller for an LED using Pulse Width Modulation (PWM) on a GPIO pin.
    
    This class wraps gpiozero.PWMLED. PWM allows for dimming the LED
    by rapidly turning the power on and off at varying duty cycles.
    """
    
    def __init__(self, pin: int, frequency: int = 100):
        """
        Initialize the PWM LED controller.
        
        Args:
            pin (int): BCM GPIO pin number.
            frequency (int): PWM frequency in Hz.
        """
        logger.info(f"Initializing PWMLED on pin {pin} (frequency={frequency}Hz)")
        self._led = PWMLED(pin, frequency=frequency)
        
    @property
    def value(self) -> float:
        """Get the current duty cycle (0.0 to 1.0)."""
        return self._led.value
        
    @value.setter
    def value(self, v: float) -> None:
        """Set the duty cycle (0.0 to 1.0)."""
        self._led.value = max(0.0, min(1.0, v))
        
    def fade_in(self, duration: float = 1.0) -> None:
        """Fade in the LED from current state to full brightness."""
        logger.info(f"Fading in PWMLED on pin {self._led.pin.number} (duration={duration}s)")
        self._led.pulse(fade_in_time=duration, fade_out_time=0.001, n=1, background=False)
        self.value = 1.0
        
    def fade_out(self, duration: float = 1.0) -> None:
        """Fade out the LED from current state to off."""
        logger.info(f"Fading out PWMLED on pin {self._led.pin.number} (duration={duration}s)")
        self._led.pulse(fade_in_time=0.001, fade_out_time=duration, n=1, background=False)
        self.value = 0.0
        
    def pulse(self, fade_in_time: float = 1.0, fade_out_time: float = 1.0, n: Optional[int] = None) -> None:
        """
        Pulse the LED in and out.
        
        Args:
            fade_in_time (float): Time to fade in.
            fade_out_time (float): Time to fade out.
            n (int, optional): Number of pulses (None means forever).
        """
        logger.info(f"Pulsing PWMLED on pin {self._led.pin.number}")
        self._led.pulse(fade_in_time=fade_in_time, fade_out_time=fade_out_time, n=n)
        
    def close(self) -> None:
        """Close the LED connection and release resources."""
        if hasattr(self, '_led') and self._led:
            logger.info(f"Closing PWMLED on pin {self._led.pin.number}")
            self._led.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
