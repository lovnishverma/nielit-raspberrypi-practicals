from nielit_rpi.gpio import LEDController, ButtonReader, BuzzerController, PWMLEDController

def test_led_controller(reset_led_mock):
    led = LEDController(17)
    assert reset_led_mock.called
    
    led.on()
    assert led._led.on.called
    
    led.off()
    assert led._led.off.called
    
    led.toggle()
    assert led._led.toggle.called
    
    led.blink(0.5, 0.5)
    assert led._led.blink.called
    
    led._led.is_lit = True
    assert led.is_lit == True
    
    led.close()
    assert led._led.close.called

def test_led_context_manager(reset_led_mock):
    with LEDController(17) as led:
        led.on()
        assert led._led.on.called
    assert led._led.close.called

def test_button_reader(reset_button_mock):
    btn = ButtonReader(18, pull_up=True, bounce_time=0.1)
    assert reset_button_mock.called
    
    btn._button.is_pressed = True
    assert btn.is_pressed == True
    
    def cb(): pass
    btn.when_pressed = cb
    assert btn._button.when_pressed == cb
    
    btn.when_released = cb
    assert btn._button.when_released == cb
    
    btn.wait_for_press(timeout=1.0)
    assert btn._button.wait_for_press.called
    
    btn.close()
    assert btn._button.close.called

def test_buzzer_controller(reset_buzzer_mock):
    buzzer = BuzzerController(22)
    assert reset_buzzer_mock.called
    
    buzzer.on()
    assert buzzer._buzzer.on.called
    
    buzzer.off()
    assert buzzer._buzzer.off.called
    
    buzzer.beep(0.1, 0.1)
    assert buzzer._buzzer.beep.called
    
    buzzer.close()
    assert buzzer._buzzer.close.called

def test_pwm_led_controller(reset_mocks):
    from sys import modules
    mock_pwm_led = modules['gpiozero'].PWMLED
    
    pwm_led = PWMLEDController(12, frequency=100)
    assert mock_pwm_led.called
    
    pwm_led.value = 0.5
    pwm_led._led.value = 0.5
    assert pwm_led._led.value == 0.5
    
    pwm_led.pulse(1, 1)
    assert pwm_led._led.pulse.called
    
    pwm_led.close()
    assert pwm_led._led.close.called
