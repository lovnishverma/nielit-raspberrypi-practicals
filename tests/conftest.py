import sys
from unittest.mock import MagicMock

# Mock all hardware-specific modules before they're imported
mock_gpiozero = MagicMock()
sys.modules['gpiozero'] = mock_gpiozero
sys.modules['gpiozero.pins'] = MagicMock()
sys.modules['gpiozero.pins.mock'] = MagicMock()

mock_smbus2 = MagicMock()
sys.modules['smbus2'] = mock_smbus2

mock_adafruit_dht = MagicMock()
sys.modules['adafruit_dht'] = mock_adafruit_dht

mock_board = MagicMock()
sys.modules['board'] = mock_board

mock_mfrc522 = MagicMock()
sys.modules['mfrc522'] = mock_mfrc522

mock_paho = MagicMock()
mock_paho_client = MagicMock()
sys.modules['paho'] = mock_paho
sys.modules['paho.mqtt'] = MagicMock()
sys.modules['paho.mqtt.client'] = mock_paho_client

mock_flask = MagicMock()
sys.modules['flask'] = mock_flask

mock_spidev = MagicMock()
sys.modules['spidev'] = mock_spidev

mock_RPi = MagicMock()
sys.modules['RPi'] = mock_RPi
sys.modules['RPi.GPIO'] = MagicMock()

import pytest
import os
import tempfile

@pytest.fixture
def reset_mocks():
    """Reset all mocks for each test."""
    mock_gpiozero.LED.reset_mock()
    mock_gpiozero.Button.reset_mock()
    mock_gpiozero.Buzzer.reset_mock()
    mock_gpiozero.PWMLED.reset_mock()
    mock_gpiozero.DistanceSensor.reset_mock()
    mock_gpiozero.MotionSensor.reset_mock()
    mock_gpiozero.MCP3008.reset_mock()
    mock_gpiozero.OutputDevice.reset_mock()
    mock_gpiozero.AngularServo.reset_mock()
    mock_smbus2.SMBus.reset_mock()
    mock_adafruit_dht.DHT11.reset_mock()
    mock_adafruit_dht.DHT22.reset_mock()
    mock_mfrc522.SimpleMFRC522.reset_mock()
    mock_paho_client.Client.reset_mock()
    yield

@pytest.fixture
def reset_led_mock(reset_mocks):
    yield mock_gpiozero.LED

@pytest.fixture
def reset_button_mock(reset_mocks):
    yield mock_gpiozero.Button

@pytest.fixture
def reset_buzzer_mock(reset_mocks):
    yield mock_gpiozero.Buzzer

@pytest.fixture
def tmp_db():
    fd, path = tempfile.mkstemp(suffix='.db')
    os.close(fd)
    yield path
    if os.path.exists(path):
        os.unlink(path)
