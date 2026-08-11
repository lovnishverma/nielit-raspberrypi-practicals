#!/usr/bin/env python3
import sys
import os
import subprocess

def check_python_version():
    return sys.version_info >= (3, 9)

def check_gpiozero():
    try:
        import gpiozero
        return True
    except ImportError:
        return False

def check_i2c():
    return os.path.exists('/dev/i2c-1')

def check_spi():
    return os.path.exists('/dev/spidev0.0')

def check_camera():
    try:
        result = subprocess.run(['vcgencmd', 'get_camera'], capture_output=True, text=True)
        if 'detected=1' in result.stdout:
            return True
        
        result2 = subprocess.run(['libcamera-hello', '--list-cameras'], capture_output=True, text=True)
        if 'Available cameras' in result2.stdout and '0 cameras' not in result2.stdout:
            return True
    except FileNotFoundError:
        pass
    return False

def is_raspberry_pi():
    try:
        with open('/sys/firmware/devicetree/base/model', 'r') as f:
            if 'Raspberry Pi' in f.read():
                return True
    except FileNotFoundError:
        pass
    return False

def main():
    print("=" * 40)
    print(" NIELIT RPi System Check ")
    print("=" * 40)
    
    checks = [
        ("Raspberry Pi Hardware", is_raspberry_pi()),
        ("Python Version >= 3.9", check_python_version()),
        ("gpiozero Installed", check_gpiozero()),
        ("I2C Enabled (/dev/i2c-1)", check_i2c()),
        ("SPI Enabled (/dev/spidev0.0)", check_spi()),
        ("Camera Detected", check_camera())
    ]
    
    for name, status in checks:
        status_str = "✅ PASS" if status else "❌ FAIL"
        print(f"{name:<30}: {status_str}")
        
    print("=" * 40)

if __name__ == '__main__':
    main()
