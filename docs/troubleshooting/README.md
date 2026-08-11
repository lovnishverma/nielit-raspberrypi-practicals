# Troubleshooting Guide

## GPIO Permission Errors
If you encounter permission denied errors when accessing GPIO:
- Ensure your user is part of the `gpio` group:
  ```bash
  sudo usermod -aG gpio $USER
  ```
- Log out and log back in for changes to take effect.

## I2C Not Detected
If the 16x2 LCD is not working:
- Ensure I2C is enabled in `sudo raspi-config`.
- Check if the device is detected:
  ```bash
  i2cdetect -y 1
  ```
  You should see an address like `0x27` or `0x3F`.

## SPI Not Enabled
If MCP3008 or RFID reader fails to initialize:
- Ensure SPI is enabled in `sudo raspi-config`.
- Check if the SPI device exists: `ls /dev/spidev0.0`

## DHT Sensor Read Failures
The DHT11 sensor is timing-sensitive and may occasionally fail to read.
- The `nielit_rpi` wrappers automatically handle retries.
- Ensure you are using the correct pin (e.g., GPIO 4) and that the 10k pull-up resistor is installed if your module doesn't have one built-in.

## MQTT Connection Issues
- Ensure your broker address is correct in the `.env` file.
- Check firewall settings if connecting to an external broker.
- For local testing, ensure `mosquitto` is running: `sudo systemctl status mosquitto`

## Camera Not Found
- Ensure the camera cable is seated correctly.
- Run `libcamera-hello` to test the camera independently.

## `gpiozero` Pin Factory Errors
If `gpiozero` complains about the pin factory (especially on newer OS versions), it might be defaulting incorrectly. The package should handle this, but you can force the `lgpio` factory by setting:
```bash
export GPIOZERO_PIN_FACTORY=lgpio
```
