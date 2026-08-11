import logging
from typing import Tuple
from mfrc522 import SimpleMFRC522

logger = logging.getLogger(__name__)

class RFIDReader:
    """
    A controller for an MFRC522 RFID reader (using SPI).
    
    This class wraps the mfrc522 library to read and write RFID tags/cards.
    Make sure SPI is enabled on your Raspberry Pi!
    """
    
    def __init__(self):
        """Initialize the RFID reader."""
        logger.info("Initializing RFID Reader (MFRC522 via SPI)")
        self._reader = SimpleMFRC522()
        
    def read(self) -> Tuple[int, str]:
        """
        Wait for a tag and read its ID and text data.
        
        Returns:
            Tuple[int, str]: The ID of the card and the text data stored on it.
        """
        logger.info("Waiting for RFID tag to read...")
        try:
            id, text = self._reader.read()
            logger.debug(f"Read tag ID {id}")
            return id, text.strip()
        except Exception as e:
            logger.error(f"Error reading RFID tag: {e}")
            raise
            
    def write(self, text: str) -> int:
        """
        Wait for a tag and write text data to it.
        
        Args:
            text (str): The text data to write to the tag.
            
        Returns:
            int: The ID of the written card.
        """
        logger.info(f"Waiting for RFID tag to write text: '{text}'...")
        try:
            id, _ = self._reader.write(text)
            logger.debug(f"Wrote to tag ID {id}")
            return id
        except Exception as e:
            logger.error(f"Error writing to RFID tag: {e}")
            raise
            
    def close(self) -> None:
        """Clean up GPIO resources used by the SPI interface."""
        import RPi.GPIO as GPIO
        logger.info("Cleaning up RFID Reader resources")
        GPIO.cleanup()
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
