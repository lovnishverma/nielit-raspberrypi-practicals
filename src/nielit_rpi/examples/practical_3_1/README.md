# Practical 3_1 — System Information

## Aim
To retrieve and display basic system information of the Raspberry Pi.

## Learning Objectives
* Understand how to query system metrics using Python.
* Learn about platform-specific information such as kernel and OS.
* Familiarize with disk usage querying.

## Components Required
* Raspberry Pi (Any model)

## Circuit Diagram / Hardware Connections
* Hardware: RPi only. No GPIO connections required.

## Software Requirements
* No extra external packages required.
* Ensure the `nielit_rpi` library is installed.

## How It Works
The script utilizes the `nielit_rpi.utilities` module's `get_system_info` function to abstract away platform-specific calls to `platform` and `shutil` modules, as well as reading the `/proc/device-tree/model` file. It returns a dictionary which is then iterated and printed.

## Running the Program
```bash
python main.py
```

## Expected Output
```text
NIELIT Raspberry Pi - System Information
Hostname: raspberrypi
Python: 3.9.2
Architecture: aarch64
OS: Linux-5.10.63-v8+-aarch64-with-glibc2.31
Kernel: 5.10.63-v8+
Model: Raspberry Pi 4 Model B Rev 1.4
Disk: 20.50 GB free / 29.70 GB
```

## Troubleshooting
* **Missing `nielit_rpi` module**: Ensure you run `pip install .` in the root of the project.
* **Unavailable Model**: If running outside of a Raspberry Pi, the model file may not exist. The script handles this gracefully.

## Safety Notes
* No special hardware safety notes for this practical.

## GPIO Reference
* All practicals use BCM numbering, though none is used here.
