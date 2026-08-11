import logging
import time
from typing import Tuple, Optional
import adafruit_dht
import board

logger = logging.getLogger(__name__)

class DHTSensor:
    """
    A controller for DHT11 or DHT22 Temperature and Humidity sensors.
    
    Wraps adafruit_dht to provide easier error handling and retries.
    """
    
    def __init__(self, pin, sensor_type: str = "DHT11"):
        """
        Initialize the DHT sensor.
        
        Args:
            pin: The adafruit board pin object (e.g., board.D4).
            sensor_type (str): "DHT11" or "DHT22".
        """
        self.sensor_type = sensor_type.upper()
        logger.info(f"Initializing {self.sensor_type} sensor on pin {pin}")
        
        if self.sensor_type == "DHT22":
            self._sensor = adafruit_dht.DHT22(pin)
        else:
            self._sensor = adafruit_dht.DHT11(pin)
            
    def read(self) -> Tuple[Optional[float], Optional[float]]:
        """
        Read temperature and humidity with retry logic.
        
        Returns:
            Tuple[float | None, float | None]: (temperature_celsius, humidity_percent)
        """
        retries = 3
        for attempt in range(retries):
            try:
                temp = self._sensor.temperature
                humidity = self._sensor.humidity
                if temp is not None and humidity is not None:
                    return temp, humidity
            except RuntimeError as error:
                # DHT sensors often fail to read, requiring retries
                logger.warning(f"DHT reading error: {error.args[0]}. Retrying...")
                time.sleep(2.0)
            except Exception as error:
                self._sensor.exit()
                logger.error(f"Fatal error from DHT sensor: {error}")
                raise error
        logger.error("Failed to read from DHT sensor after retries.")
        return None, None
        
    @property
    def temperature(self) -> Optional[float]:
        """Get the current temperature in Celsius."""
        temp, _ = self.read()
        return temp
        
    @property
    def humidity(self) -> Optional[float]:
        """Get the current humidity percentage."""
        _, hum = self.read()
        return hum
        
    def close(self) -> None:
        """Release resources used by the DHT sensor."""
        if hasattr(self, '_sensor') and self._sensor:
            logger.info(f"Closing {self.sensor_type} sensor")
            self._sensor.exit()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
