"""
Practical 3.17: Flask GPIO Web Control

This practical demonstrates controlling a GPIO LED via a simple web interface using Flask.
"""
from flask import Flask, redirect, url_for, render_template_string
from gpiozero import LED

# Configuration
LED_PIN = 17
app = Flask(__name__)
led = None

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>NIELIT GPIO Control</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        .btn { padding: 15px 30px; font-size: 20px; text-decoration: none; border-radius: 5px; color: white; margin: 10px; }
        .btn-on { background-color: #4CAF50; }
        .btn-off { background-color: #f44336; }
    </style>
</head>
<body>
    <h1>NIELIT Raspberry Pi Web Control</h1>
    <h2>LED Status: <strong>{{state}}</strong></h2>
    <br>
    <a href="/led/on" class="btn btn-on">Turn ON</a>
    <a href="/led/off" class="btn btn-off">Turn OFF</a>
</body>
</html>
"""

@app.route("/")
def index():
    """Renders the main control page."""
    current_state = "ON" if led.is_lit else "OFF"
    return render_template_string(PAGE_TEMPLATE, state=current_state)

@app.route("/led/<state>")
def control(state: str):
    """Handles commands to turn the LED on or off."""
    state = state.lower()
    if state == "on":
        led.on()
    elif state == "off":
        led.off()
    else:
        return "Invalid state. Use 'on' or 'off'.", 400
    
    # Redirect back to the index page to update the status
    return redirect(url_for("index"))

def main() -> None:
    """Main execution block."""
    global led
    print("Starting Flask GPIO Web Control Practical...")
    try:
        led = LED(LED_PIN)
        print(f"LED initialized on GPIO {LED_PIN}.")
        print("Starting web server. Access it via http://<raspberry-pi-ip>:5000")
        
        # Run Flask development server on all network interfaces
        app.run(host="0.0.0.0", port=5000, debug=False)
        
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Cleaning up GPIO resources...")
        if led:
            led.off()
            led.close()
        print("Done.")

if __name__ == "__main__":
    main()
