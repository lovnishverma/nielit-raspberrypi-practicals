import logging
from gpiozero import OutputDevice

logger = logging.getLogger(__name__)

class RelayController:
    """
    A controller for an electromechanical relay module.
    
    WARNING: Do NOT connect mains electricity (120V/240V AC) to standard hobby relays 
    unless you are a qualified electrician. This module is for controlling low-voltage DC 
    or safely isolated circuits for educational purposes.
    
    Wraps gpiozero.OutputDevice for relay control.
    """
    
    def __init__(self, pin: int, active_high: bool = True):
        """
        Initialize the Relay controller.
        
        Args:
            pin (int): BCM GPIO pin number.
            active_high (bool): If True, setting pin HIGH activates the relay.
                                Some relay modules are active LOW.
        """
        logger.info(f"Initializing Relay on pin {pin} (active_high={active_high})")
        self._relay = OutputDevice(pin, active_high=active_high, initial_value=False)
        
    def on(self) -> None:
        """Activate the relay."""
        logger.info(f"Activating Relay on pin {self._relay.pin.number}")
        self._relay.on()
        
    def off(self) -> None:
        """Deactivate the relay."""
        logger.info(f"Deactivating Relay on pin {self._relay.pin.number}")
        self._relay.off()
        
    def toggle(self) -> None:
        """Toggle the relay state."""
        logger.info(f"Toggling Relay on pin {self._relay.pin.number}")
        self._relay.toggle()
        
    @property
    def is_active(self) -> bool:
        """Return True if the relay is active."""
        return self._relay.value == 1
        
    def close(self) -> None:
        """Release resources used by the relay."""
        if hasattr(self, '_relay') and self._relay:
            logger.info(f"Closing Relay on pin {self._relay.pin.number}")
            self._relay.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
