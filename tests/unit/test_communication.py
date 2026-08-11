from nielit_rpi.communication import RFIDReader, MQTTPublisher, MQTTSubscriber
from unittest.mock import MagicMock

def test_rfid_reader(reset_mocks):
    from sys import modules
    mock_mfrc522 = modules['mfrc522'].SimpleMFRC522
    
    reader = RFIDReader()
    
    # Mock read
    reader._reader.read = MagicMock(return_value=(12345, "Test Data"))
    
    res = reader.read()
    assert res is not None
    
    # Mock write
    reader._reader.write = MagicMock(return_value=(12345, "Hello"))
    reader.write("Hello")
    assert reader._reader.write.called
    
    reader.close()

def test_mqtt_publisher(reset_mocks):
    from sys import modules
    mock_client_class = modules['paho.mqtt.client'].Client
    
    pub = MQTTPublisher("localhost", 1883, "test/topic")
    pub.connect()
    assert pub.client.connect.called
    
    pub.publish("Hello")
    assert pub.client.publish.called
    
    pub.disconnect()
    assert pub.client.disconnect.called

def test_mqtt_subscriber(reset_mocks):
    from sys import modules
    mock_client_class = modules['paho.mqtt.client'].Client
    
    def cb(msg): pass
    sub = MQTTSubscriber("localhost", 1883, "test/topic", cb)
    
    sub.connect()
    assert sub.client.connect.called
    
    sub.start()
    assert sub.client.loop_start.called
    
    sub.stop()
    assert sub.client.loop_stop.called
    
    sub.disconnect()
    assert sub.client.disconnect.called
