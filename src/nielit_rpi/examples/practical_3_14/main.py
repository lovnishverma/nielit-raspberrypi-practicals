"""
Practical 3.14: LDR + MCP3008 ADC

This practical reads analog light levels using an MCP3008 SPI ADC.
"""
import time
from nielit_rpi.sensors import LDRSensor

# Constants
ADC_CHANNEL = 0
DELAY = 0.5

def main() -> None:
    """Main execution function."""
    print("Starting LDR + MCP3008 ADC Practical...")
    ldr = None
    try:
        # Initialize LDR sensor on MCP3008 channel 0
        ldr = LDRSensor(channel=ADC_CHANNEL)
        print("Reading light levels. Press Ctrl+C to exit.")
        
        while True:
            # LDRSensor returns a normalized value (0.0 to 1.0) and computed voltage
            val = ldr.value
            volts = ldr.voltage
            print(f"LDR Value: {val:.3f} | Voltage: {volts:.3f} V")
            time.sleep(DELAY)
            
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    finally:
        print("Cleaning up SPI resources...")
        if ldr:
            ldr.close()
        print("Done.")

if __name__ == "__main__":
    main()
