import time
import logging
from smbus2 import SMBus

logger = logging.getLogger(__name__)

# LCD Instructions
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# Flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# Flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# Flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# Flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# Flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

# Control flags
ENABLE = 0b00000100  # Enable bit

class I2CLCD:
    """
    A controller for an I2C-connected 16x2 character LCD.
    
    This class communicates directly via the SMBus (I2C) interface to send commands 
    and data to the LCD backpack controller (often a PCF8574).
    """
    
    def __init__(self, address: int = 0x27, bus_number: int = 1, width: int = 16, lines: int = 2):
        """
        Initialize the I2C LCD controller.
        
        Args:
            address (int): I2C address of the display (typically 0x27 or 0x3f).
            bus_number (int): The I2C bus number (typically 1 on Raspberry Pi).
            width (int): Number of characters per line.
            lines (int): Number of lines on the display.
        """
        self.address = address
        self.width = width
        self.lines = lines
        self.bus = SMBus(bus_number)
        self.backlight = LCD_BACKLIGHT
        
        logger.info(f"Initializing I2C LCD at address 0x{address:02x}")
        self.init()
        
    def init(self) -> None:
        """Initialize the display."""
        try:
            self._send_byte(0x03, 0)
            self._send_byte(0x03, 0)
            self._send_byte(0x03, 0)
            self._send_byte(0x02, 0)
            
            self._send_byte(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE, 0)
            self._send_byte(LCD_DISPLAYCONTROL | LCD_DISPLAYON, 0)
            self._send_byte(LCD_CLEARDISPLAY, 0)
            self._send_byte(LCD_ENTRYMODESET | LCD_ENTRYLEFT, 0)
            time.sleep(0.2)
        except Exception as e:
            logger.error(f"Failed to initialize LCD: {e}")
            raise
            
    def _send_byte(self, bits: int, mode: int) -> None:
        """
        Send a byte to data pins.
        
        Args:
            bits (int): Data to send.
            mode (int): 1 for data, 0 for command.
        """
        bits_high = mode | (bits & 0xF0) | self.backlight
        bits_low = mode | ((bits << 4) & 0xF0) | self.backlight
        
        self.bus.write_byte(self.address, bits_high)
        self._toggle_enable(bits_high)
        
        self.bus.write_byte(self.address, bits_low)
        self._toggle_enable(bits_low)
        
    def _toggle_enable(self, bits: int) -> None:
        """Toggle the enable bit."""
        time.sleep(0.0005)
        self.bus.write_byte(self.address, (bits | ENABLE))
        time.sleep(0.0005)
        self.bus.write_byte(self.address, (bits & ~ENABLE))
        time.sleep(0.0005)
        
    def clear(self) -> None:
        """Clear the display."""
        logger.debug("Clearing LCD")
        self._send_byte(LCD_CLEARDISPLAY, 0)
        time.sleep(0.002) # Clear requires extra time
        
    def write_string(self, text: str, line: int = 1) -> None:
        """
        Write a string to a specific line.
        
        Args:
            text (str): The text to display.
            line (int): The line number (1 or 2).
        """
        if line == 1:
            self._send_byte(LCD_SETDDRAMADDR | 0x00, 0)
        elif line == 2:
            self._send_byte(LCD_SETDDRAMADDR | 0x40, 0)
            
        text = text.ljust(self.width, " ")
        for i in range(self.width):
            self._send_byte(ord(text[i]), 1)
            
    def backlight_on(self) -> None:
        """Turn on the backlight."""
        self.backlight = LCD_BACKLIGHT
        self.bus.write_byte(self.address, self.backlight)
        
    def backlight_off(self) -> None:
        """Turn off the backlight."""
        self.backlight = LCD_NOBACKLIGHT
        self.bus.write_byte(self.address, self.backlight)
        
    def close(self) -> None:
        """Clear display, turn off backlight, and release bus."""
        logger.info("Closing I2C LCD connection")
        try:
            self.clear()
            self.backlight_off()
            self.bus.close()
        except Exception as e:
            logger.error(f"Error closing LCD: {e}")
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
