import logging
from typing import Tuple
from flask import Flask, render_template_string
from gpiozero import LED

logger = logging.getLogger(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raspberry Pi GPIO Control</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
        .btn { padding: 15px 32px; font-size: 24px; margin: 10px; cursor: pointer; border: none; border-radius: 8px; color: white; }
        .btn-on { background-color: #4CAF50; }
        .btn-off { background-color: #f44336; }
        .status { font-size: 20px; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Raspberry Pi LED Control</h1>
    <div>
        <form action="/led/on" method="POST" style="display: inline;">
            <button class="btn btn-on" type="submit">Turn ON</button>
        </form>
        <form action="/led/off" method="POST" style="display: inline;">
            <button class="btn btn-off" type="submit">Turn OFF</button>
        </form>
    </div>
    <div class="status">
        Current State: {% if is_lit %} ON {% else %} OFF {% endif %}
    </div>
</body>
</html>
"""

def create_gpio_web_app(led_pin: int = 17, host: str = '0.0.0.0', port: int = 5000) -> Tuple[Flask, LED]:
    """
    Create a Flask web application for controlling an LED.
    
    Args:
        led_pin (int): BCM GPIO pin number for the LED.
        host (str): Host interface to bind to (default '0.0.0.0' for all interfaces).
        port (int): Port to run the server on.
        
    Returns:
        Tuple[Flask, LED]: The Flask app instance and the LED instance so they can be managed/closed.
    """
    app = Flask(__name__)
    led = LED(led_pin)
    
    logger.info(f"Creating GPIO Web App (LED pin={led_pin}, Host={host}, Port={port})")
    
    @app.route('/')
    def index():
        return render_template_string(HTML_TEMPLATE, is_lit=led.is_lit)
        
    @app.route('/led/<state>', methods=['POST'])
    def control_led(state):
        if state == 'on':
            led.on()
            logger.info("Web interface: Turned LED ON")
        elif state == 'off':
            led.off()
            logger.info("Web interface: Turned LED OFF")
        return render_template_string(HTML_TEMPLATE, is_lit=led.is_lit)
        
    # Store config in app context for convenience if needed later
    app.config['HOST'] = host
    app.config['PORT'] = port
    
    return app, led
