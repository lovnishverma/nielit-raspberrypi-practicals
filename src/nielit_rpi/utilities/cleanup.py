"""GPIO cleanup utilities."""
import logging
from typing import Any, List

logger = logging.getLogger(__name__)


def cleanup_devices(*devices: Any) -> None:
    """
    Close multiple GPIO devices safely.
    
    Args:
        *devices: Variable number of gpiozero device objects.
    """
    for device in devices:
        if device is not None:
            try:
                device.close()
                logger.debug("Closed device: %s", device)
            except Exception as e:
                logger.warning("Failed to close device %s: %s", device, e)


class GPIOCleanup:
    """
    Context manager to ensure safe cleanup of GPIO resources.
    
    Example:
        led = LED(17)
        with GPIOCleanup([led]):
            led.on()
            sleep(1)
    """

    def __init__(self, devices: List[Any]):
        """
        Initialize the context manager.
        
        Args:
            devices: A list of gpiozero device objects to clean up.
        """
        self.devices = devices

    def __enter__(self) -> "GPIOCleanup":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Clean up resources on exit."""
        logger.info("Cleaning up GPIO resources...")
        cleanup_devices(*self.devices)
