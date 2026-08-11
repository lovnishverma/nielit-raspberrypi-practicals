import logging
from gpiozero import MCP3008

logger = logging.getLogger(__name__)

class LDRSensor:
    """
    A controller for an LDR (Light Dependent Resistor) connected via MCP3008 ADC.
    
    Wraps gpiozero.MCP3008.
    """
    
    def __init__(self, channel: int = 0):
        """
        Initialize the LDR sensor on the ADC.
        
        Args:
            channel (int): MCP3008 channel (0-7) where LDR voltage divider is connected.
        """
        logger.info(f"Initializing LDR on MCP3008 channel {channel}")
        self._adc = MCP3008(channel=channel)
        
    @property
    def value(self) -> float:
        """Return the normalized value (0.0 to 1.0) from the ADC."""
        return self._adc.value
        
    @property
    def voltage(self) -> float:
        """Return the approximate voltage (assuming 3.3V reference)."""
        return self._adc.value * 3.3
        
    def close(self) -> None:
        """Close the ADC connection and release resources."""
        if hasattr(self, '_adc') and self._adc:
            logger.info("Closing LDR/MCP3008 sensor")
            self._adc.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
