from nielit_rpi.displays import I2CLCD

def test_i2c_lcd(reset_mocks):
    from sys import modules
    mock_bus = modules['smbus2'].SMBus
    
    lcd = I2CLCD(address=0x27, bus_number=1)
    
    lcd.write_string("Hello")
    
    lcd.clear()
    
    lcd.close()
    lcd.bus.close.assert_called_once()
