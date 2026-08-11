from nielit_rpi.sensors import UltrasonicSensor, PIRSensor, LDRSensor, DHTSensor

def test_ultrasonic_sensor(reset_mocks):
    from sys import modules
    mock_sensor = modules['gpiozero'].DistanceSensor
    
    sensor = UltrasonicSensor(trigger_pin=23, echo_pin=24, max_distance=2.0)
    assert mock_sensor.called
    
    sensor._sensor.distance = 1.5
    assert sensor.distance_m == 1.5
    
    assert sensor.in_range(threshold_cm=200) == True
    
    sensor.close()
    assert sensor._sensor.close.called

def test_pir_sensor(reset_mocks):
    from sys import modules
    mock_sensor = modules['gpiozero'].MotionSensor
    
    sensor = PIRSensor(25)
    assert mock_sensor.called
    
    sensor._sensor.motion_detected = True
    assert sensor.motion_detected == True
    
    def cb(): pass
    sensor.when_motion = cb
    assert sensor._sensor.when_motion == cb
    
    sensor.when_no_motion = cb
    assert sensor._sensor.when_no_motion == cb
    
    sensor.close()
    assert sensor._sensor.close.called

def test_ldr_sensor(reset_mocks):
    from sys import modules
    mock_sensor = modules['gpiozero'].MCP3008
    
    sensor = LDRSensor(0)
    assert mock_sensor.called
    
    if hasattr(sensor, '_sensor'):
        sensor._sensor.value = 0.5
    elif hasattr(sensor, '_adc'):
        sensor._adc.value = 0.5
        
    sensor.close()
    if hasattr(sensor, '_sensor'):
        assert sensor._sensor.close.called
    elif hasattr(sensor, '_adc'):
        assert sensor._adc.close.called

def test_dht_sensor(reset_mocks):
    from sys import modules
    mock_dht11 = modules['adafruit_dht'].DHT11
    
    sensor = DHTSensor(4, sensor_type='DHT11')
    
    sensor._sensor.temperature = 25.0
    sensor._sensor.humidity = 60.0
    
    assert sensor.temperature == 25.0
    assert sensor.humidity == 60.0
    
    sensor.close()
    assert sensor._sensor.exit.called
