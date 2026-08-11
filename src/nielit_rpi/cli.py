"""CLI utility for executing NIELIT Raspberry Pi practicals."""
import argparse
import sys
import os
import subprocess
from .utilities.system_info import get_system_info

# Registry of practicals
PRACTICALS = {
    "3_1": {"title": "System Information", "hardware": "RPi only", "difficulty": "Beginner"},
    "3_2": {"title": "GPIO LED Output", "hardware": "LED + resistor", "difficulty": "Beginner"},
    "3_3": {"title": "Push Button Input", "hardware": "Push button", "difficulty": "Beginner"},
    "3_4": {"title": "Button Controlled LED", "hardware": "Button + LED", "difficulty": "Beginner"},
    "3_5": {"title": "Traffic Light Controller", "hardware": "3 LEDs", "difficulty": "Beginner"},
    "3_6": {"title": "PWM LED Brightness", "hardware": "LED", "difficulty": "Beginner"},
    "3_7": {"title": "Buzzer Alert", "hardware": "Active buzzer", "difficulty": "Beginner"},
    "3_8": {"title": "Servo Motor Control", "hardware": "SG90 servo", "difficulty": "Intermediate"},
    "3_9": {"title": "HC-SR04 Distance", "hardware": "HC-SR04 sensor", "difficulty": "Intermediate"},
    "3_10": {"title": "DHT11 Temp & Humidity", "hardware": "DHT11 sensor", "difficulty": "Intermediate"},
    "3_11": {"title": "I2C LCD Display", "hardware": "16x2 I2C LCD", "difficulty": "Intermediate"},
    "3_12": {"title": "PIR Motion Detection", "hardware": "PIR sensor", "difficulty": "Intermediate"},
    "3_13": {"title": "Relay Control", "hardware": "Relay module", "difficulty": "Intermediate"},
    "3_14": {"title": "LDR + MCP3008 ADC", "hardware": "MCP3008 + LDR", "difficulty": "Intermediate"},
    "3_15": {"title": "MFRC522 RFID", "hardware": "MFRC522 module", "difficulty": "Advanced"},
    "3_16": {"title": "SQLite Sensor Logger", "hardware": "RPi only", "difficulty": "Intermediate"},
    "3_17": {"title": "Flask GPIO Web Control", "hardware": "LED + LAN", "difficulty": "Advanced"},
    "3_18": {"title": "MQTT Publisher", "hardware": "Network", "difficulty": "Advanced"},
    "3_19": {"title": "MQTT Subscriber + GPIO", "hardware": "LED + MQTT", "difficulty": "Advanced"},
    "3_20": {"title": "Smart Home Capstone", "hardware": "PIR + LED", "difficulty": "Advanced"},
}


def cmd_list() -> None:
    """List all available practicals."""
    print(f"{'ID':<6} | {'Title':<30} | {'Hardware':<20} | {'Difficulty':<15}")
    print("-" * 80)
    for p_id, data in PRACTICALS.items():
        print(f"{p_id:<6} | {data['title']:<30} | {data['hardware']:<20} | {data['difficulty']:<15}")


def cmd_info(practical_id: str) -> None:
    """Show details for a specific practical."""
    if practical_id not in PRACTICALS:
        print(f"Error: Practical '{practical_id}' not found.")
        sys.exit(1)
        
    data = PRACTICALS[practical_id]
    print(f"Practical ID : {practical_id}")
    print(f"Title        : {data['title']}")
    print(f"Hardware     : {data['hardware']}")
    print(f"Difficulty   : {data['difficulty']}")


def cmd_check() -> None:
    """Check system compatibility."""
    print("--- System Check ---")
    info = get_system_info()
    print(f"Hostname: {info['hostname']}")
    print(f"Python version: {info['python_version']}")
    print(f"Model: {info['model']}")
    
    print("\n--- Dependencies ---")
    try:
        import gpiozero
        print("[OK] gpiozero is installed")
    except ImportError:
        print("[FAIL] gpiozero is NOT installed")
        
    print("\n--- Hardware Interfaces ---")
    if os.path.exists("/dev/i2c-1"):
        print("[OK] I2C interface (/dev/i2c-1) is enabled")
    else:
        print("[FAIL] I2C interface is NOT enabled")
        
    if os.path.exists("/dev/spidev0.0"):
        print("[OK] SPI interface (/dev/spidev0.0) is enabled")
    else:
        print("[FAIL] SPI interface is NOT enabled")


def cmd_run(practical_id: str) -> None:
    """Run a specific practical."""
    if practical_id not in PRACTICALS:
        print(f"Error: Practical '{practical_id}' not found.")
        sys.exit(1)
        
    data = PRACTICALS[practical_id]
    print(f"Preparing to run: {data['title']}")
    
    if "RPi only" not in data['hardware'] and "Network" not in data['hardware']:
        print(f"\nWARNING: This practical requires hardware: {data['hardware']}")
        confirm = input("Are you sure you have the hardware connected correctly? (y/N): ")
        if confirm.lower() != 'y':
            print("Execution cancelled.")
            sys.exit(0)
            
    # Search for the practical's main.py in several locations:
    # 1. Current working directory examples/ (allows local student edits)
    # 2. Packaged internal examples/ directory (works anywhere when pip installed)
    # 3. Project repository root examples/ directory
    practical_dir = f"practical_{practical_id}"
    
    pkg_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(pkg_dir, "..", ".."))
    
    search_paths = [
        os.path.join(os.getcwd(), "examples", practical_dir, "main.py"),
        os.path.join(pkg_dir, "examples", practical_dir, "main.py"),
        os.path.join(project_root, "examples", practical_dir, "main.py"),
    ]
    
    main_py_path = None
    for path in search_paths:
        if os.path.exists(path):
            main_py_path = path
            break
    
    if main_py_path is None:
        print(f"\nError: Could not find practical '{practical_id}' in:")
        for p in search_paths:
            print(f"  - {p}")
        print("\nHint: You can export all practicals to your current folder by running:")
        print("  nielit-rpi export-examples")
        sys.exit(1)
        
    print(f"Executing {main_py_path}...\n" + "-"*40)
    try:
        subprocess.run([sys.executable, main_py_path], check=True)
    except KeyboardInterrupt:
        print("\nExecution stopped by user.")
    except subprocess.CalledProcessError as e:
        print(f"\nExecution failed with code {e.returncode}")


def cmd_export_examples(destination: str = "examples") -> None:
    """Export bundled practicals to a local directory for editing."""
    pkg_dir = os.path.dirname(os.path.abspath(__file__))
    src_examples = os.path.join(pkg_dir, "examples")
    
    if not os.path.exists(src_examples):
        # Fallback to repo root if running from source tree
        src_examples = os.path.abspath(os.path.join(pkg_dir, "..", "..", "examples"))
        
    if not os.path.exists(src_examples):
        print("Error: Could not locate bundled examples directory.")
        sys.exit(1)
        
    dest_path = os.path.abspath(destination)
    print(f"Exporting 20 NIELIT practicals to: {dest_path}")
    
    import shutil
    for item in sorted(os.listdir(src_examples)):
        if item.startswith("practical_"):
            s = os.path.join(src_examples, item)
            d = os.path.join(dest_path, item)
            if os.path.isdir(s):
                os.makedirs(d, exist_ok=True)
                for f in os.listdir(s):
                    if f.startswith("__") or f.endswith(".pyc"):
                        continue
                    src_file = os.path.join(s, f)
                    if os.path.isfile(src_file):
                        shutil.copy2(src_file, os.path.join(d, f))
                print(f"  [+] {item}")
                
    print(f"\nSuccessfully exported all practicals to '{destination}/'.")
    print("You can now edit and run them locally:")
    print(f"  cd {destination}/practical_3_2")
    print("  python main.py")


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="NIELIT Raspberry Pi Practicals CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # List command
    subparsers.add_parser("list", help="List all available practicals")
    
    # Info command
    info_parser = subparsers.add_parser("info", help="Show details for a specific practical")
    info_parser.add_argument("practical_id", help="The ID of the practical (e.g., 3_1, 3_2)")
    
    # Check command
    subparsers.add_parser("check", help="Check system and hardware capability")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run a specific practical")
    run_parser.add_argument("practical_id", help="The ID of the practical (e.g., 3_1, 3_2)")
    
    # Export examples command
    export_parser = subparsers.add_parser("export-examples", help="Export all practical example files to local directory")
    export_parser.add_argument("--dest", "-d", default="examples", help="Destination directory (default: examples)")
    
    args = parser.parse_args()
    
    if args.command == "list":
        cmd_list()
    elif args.command == "info":
        cmd_info(args.practical_id)
    elif args.command == "check":
        cmd_check()
    elif args.command == "run":
        cmd_run(args.practical_id)
    elif args.command == "export-examples":
        cmd_export_examples(args.dest)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
