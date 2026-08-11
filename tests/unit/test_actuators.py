from nielit_rpi.actuators import RelayController, ServoController

def test_relay_controller(reset_mocks):
    from sys import modules
    mock_relay = modules['gpiozero'].OutputDevice
    
    relay = RelayController(17, active_high=True)
    assert mock_relay.called
    
    relay.on()
    if hasattr(relay, '_device'):
        assert relay._device.on.called
    elif hasattr(relay, '_relay'):
        assert relay._relay.on.called
    
    relay.off()
    if hasattr(relay, '_device'):
        assert relay._device.off.called
    elif hasattr(relay, '_relay'):
        assert relay._relay.off.called
        
    relay.close()

def test_servo_controller(reset_mocks):
    from sys import modules
    mock_servo = modules['gpiozero'].AngularServo
    
    servo = ServoController(18)
    servo._servo.min_angle = -90
    servo._servo.max_angle = 90
    assert mock_servo.called
    
    servo.angle = 45
    assert servo._servo.angle == 45
    
    servo.min()
    assert servo._servo.min.called
    
    servo.max()
    assert servo._servo.max.called
    
    servo.close()
    assert servo._servo.close.called
