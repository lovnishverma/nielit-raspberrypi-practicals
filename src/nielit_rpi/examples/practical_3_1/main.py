"""
Practical 3_1: System Information.

This script fetches and displays various system information metrics
such as hostname, python version, architecture, OS, kernel, model,
and disk usage using the nielit_rpi library.
"""
import sys
from typing import Any
from nielit_rpi.utilities import get_system_info

def main() -> None:
    """Main function to print system information."""
    print("NIELIT Raspberry Pi - System Information")
    try:
        sys_info: dict[str, Any] = get_system_info()
        for key, value in sys_info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error retrieving system information: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
