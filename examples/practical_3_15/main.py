"""
Practical 3.15: MFRC522 RFID

This practical demonstrates reading MIFARE RFID tags using the RC522 module.
"""
from nielit_rpi.communication import RFIDReader

def main() -> None:
    """Main execution function."""
    print("Starting MFRC522 RFID Practical...")
    reader = None
    try:
        reader = RFIDReader()
        print("Place an RFID card/tag near the reader.")
        
        # read() is a blocking call waiting for a card
        card_id, text = reader.read()
        
        print(f"Card ID: {card_id}")
        print(f"Stored Text: {text.strip()}")
        
    except ImportError as e:
        print(f"Import Error: {e}. Please install the required packages.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Cleaning up GPIO resources...")
        if reader:
            # Proper cleanup of GPIO/SPI resources
            reader.close()
        print("Done.")

if __name__ == "__main__":
    main()
