/**
 * NIELIT Raspberry Pi Practicals - Complete Structured Database
 * Contains all 20 practicals with aims, circuits, code, commands, outputs, and safety notes.
 */
const PRACTICALS_DATA = [
  {
    id: "3_1",
    num: "3.1",
    title: "System Information & Diagnostics",
    category: "System",
    difficulty: "Beginner",
    hardware: "Raspberry Pi only (no extra wiring)",
    pins: [],
    protocols: ["System OS / Linux VFS"],
    dependencies: ["platform", "shutil"],
    aim: "Query, extract, and display core hardware, OS, architecture, kernel, and storage details of the Raspberry Pi.",
    objectives: [
      "Understand how Linux exposes board information via /proc and sysfs",
      "Learn Python's platform and shutil modules for system introspection",
      "Format storage and memory metrics into human-readable units",
      "Identify Raspberry Pi board revision and Python runtime version"
    ],
    components: [
      "Raspberry Pi (any model: 3B/3B+/4B/5)",
      "MicroSD Card with Raspberry Pi OS",
      "Power Supply"
    ],
    wiring: [
      { component: "Raspberry Pi Board", pin: "N/A", note: "No external GPIO connection required" }
    ],
    code: `"""
Practical 3_1: System Information.
Demonstrates reading system, board, and storage metrics using Python standard library.
"""
from nielit_rpi.utilities import get_system_info

def main() -> None:
    print("=" * 50)
    print("   NIELIT Raspberry Pi - System Diagnostics")
    print("=" * 50)
    
    info = get_system_info()
    for key, value in info.items():
        if key == "disk_usage":
            print(f"{key:<15}: {value['free_gb']:.2f} GB free / {value['total_gb']:.2f} GB total")
        else:
            print(f"{key:<15}: {value}")
            
    print("=" * 50)

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_1",
    expectedOutput: `==================================================
   NIELIT Raspberry Pi - System Diagnostics
==================================================
hostname       : raspberrypi
python_version : 3.11.2
architecture   : aarch64
os             : Linux
kernel         : 6.1.0-rpi7-rpi-v8
model          : Raspberry Pi 4 Model B Rev 1.5
disk_usage     : 24.85 GB free / 29.12 GB total
==================================================`,
    troubleshooting: [
      "If 'model' shows 'Unknown', ensure permissions allow reading /proc/device-tree/model.",
      "If running inside a non-RPi virtual machine, platform metrics will reflect the host VM."
    ],
    safetyNotes: "Always shut down the Raspberry Pi safely using 'sudo poweroff' before removing power to prevent SD card corruption."
  },
  {
    id: "3_2",
    num: "3.2",
    title: "GPIO Digital Output - LED Blink",
    category: "GPIO",
    difficulty: "Beginner",
    hardware: "LED + 220Ω/330Ω Resistor",
    pins: [17],
    protocols: ["Digital Output (3.3V Logic)"],
    dependencies: ["gpiozero"],
    aim: "Interface a light-emitting diode (LED) to a GPIO pin and toggle it ON and OFF in a periodic cycle.",
    objectives: [
      "Understand GPIO output states: HIGH (3.3V) and LOW (0V)",
      "Calculate current-limiting resistor values using Ohm's Law (V = IR)",
      "Implement non-blocking and periodic timing in Python",
      "Ensure clean GPIO pin state cleanup on exit"
    ],
    components: [
      "Raspberry Pi",
      "5mm Red/Green LED",
      "220Ω or 330Ω Resistor (1/4W)",
      "Solderless Breadboard",
      "Male-to-Female Jumper Wires"
    ],
    wiring: [
      { component: "LED Anode (Long Leg +)", pin: "GPIO 17 (Pin 11)", note: "Connect via 330Ω current-limiting resistor" },
      { component: "LED Cathode (Short Leg -)", pin: "GND (Pin 6 or Pin 9)", note: "Direct connection to Ground rail" }
    ],
    code: `"""
Practical 3_2: GPIO LED Output.
Blinks an LED connected to GPIO 17 at 1-second intervals.
"""
import time
from nielit_rpi.gpio import LEDController

LED_PIN: int = 17
BLINK_INTERVAL_SEC: float = 1.0

def main() -> None:
    print(f"Starting LED Blink on BCM GPIO {LED_PIN}. Press Ctrl+C to stop.")
    led = LEDController(pin=LED_PIN)
    try:
        while True:
            led.on()
            print("LED State: ON [HIGH - 3.3V]")
            time.sleep(BLINK_INTERVAL_SEC)
            
            led.off()
            print("LED State: OFF [LOW - 0V]")
            time.sleep(BLINK_INTERVAL_SEC)
    except KeyboardInterrupt:
        print("\\nBlink interrupted by user.")
    finally:
        led.close()
        print("GPIO resources safely released.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_2",
    expectedOutput: `Starting LED Blink on BCM GPIO 17. Press Ctrl+C to stop.
LED State: ON [HIGH - 3.3V]
LED State: OFF [LOW - 0V]
LED State: ON [HIGH - 3.3V]
LED State: OFF [LOW - 0V]
^C
Blink interrupted by user.
GPIO resources safely released.`,
    troubleshooting: [
      "LED does not light up: Check LED polarity (longer lead is positive Anode).",
      "Dim LED: Verify resistor value is not too high (use 220Ω–330Ω, avoid >1kΩ for indicators).",
      "Pin busy error: Ensure another background script is not currently using GPIO 17."
    ],
    safetyNotes: "NEVER connect an LED directly between GPIO and GND without a current-limiting resistor; exceeding 16mA per pin will damage the SoC."
  },
  {
    id: "3_3",
    num: "3.3",
    title: "Push Button Digital Input",
    category: "GPIO",
    difficulty: "Beginner",
    hardware: "Tactile Push Button",
    pins: [27],
    protocols: ["Digital Input with Internal Pull-Up"],
    dependencies: ["gpiozero"],
    aim: "Read digital input signals from a tactile push button using internal pull-up resistors.",
    objectives: [
      "Understand floating inputs and the role of pull-up/pull-down resistors",
      "Configure internal SoC pull-up resistors in software",
      "Detect button press and release transitions",
      "Handle mechanical contact bouncing in software"
    ],
    components: [
      "Raspberry Pi",
      "Tactile Push Button Switch",
      "Breadboard and Jumper Wires"
    ],
    wiring: [
      { component: "Button Terminal 1", pin: "GPIO 27 (Pin 13)", note: "Configured with internal pull-up" },
      { component: "Button Terminal 2", pin: "GND (Pin 14)", note: "Closing switch pulls pin to 0V (Active LOW)" }
    ],
    code: `"""
Practical 3_3: Push Button Input.
Monitors digital state of a button connected to GPIO 27 with pull-up.
"""
import time
from nielit_rpi.gpio import ButtonReader

BUTTON_PIN: int = 27

def main() -> None:
    print(f"Reading Button on GPIO {BUTTON_PIN}. Press button or Ctrl+C to exit.")
    button = ButtonReader(pin=BUTTON_PIN, pull_up=True, bounce_time=0.05)
    
    try:
        while True:
            if button.is_pressed:
                print("Button State: [ PRESSED  ]", end="\\r", flush=True)
            else:
                print("Button State: [ RELEASED ]", end="\\r", flush=True)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\\nExiting input monitor.")
    finally:
        button.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_3",
    expectedOutput: `Reading Button on GPIO 27. Press button or Ctrl+C to exit.
Button State: [ PRESSED  ]
Button State: [ RELEASED ]
^C
Exiting input monitor.`,
    troubleshooting: [
      "State stays 'PRESSED': Ensure button legs are oriented correctly across breadboard center trough.",
      "Erratic/glitchy readings: Increase software debounce time (e.g. bounce_time=0.05s)."
    ],
    safetyNotes: "Always connect button to GND when using internal pull-up. Never connect external 5V to GPIO input pins."
  },
  {
    id: "3_4",
    num: "3.4",
    title: "Button-Controlled LED Interfacing",
    category: "GPIO",
    difficulty: "Beginner",
    hardware: "Tactile Button + LED + Resistor",
    pins: [17, 27],
    protocols: ["Event-Driven Digital I/O"],
    dependencies: ["gpiozero"],
    aim: "Implement asynchronous event-driven control where pressing a push button illuminates an LED.",
    objectives: [
      "Combine input and output peripherals in a single application",
      "Understand callback-driven / interrupt-based programming vs polling",
      "Use signals to pause the main thread efficiently without CPU spinlocks"
    ],
    components: [
      "Raspberry Pi",
      "Push Button",
      "LED + 330Ω Resistor",
      "Breadboard and Jumper Wires"
    ],
    wiring: [
      { component: "LED Anode (+)", pin: "GPIO 17 (Pin 11)", note: "Via 330Ω resistor" },
      { component: "LED Cathode (-)", pin: "GND (Pin 9)", note: "To Ground" },
      { component: "Button Terminal 1", pin: "GPIO 27 (Pin 13)", note: "Internal pull-up enabled" },
      { component: "Button Terminal 2", pin: "GND (Pin 14)", note: "To Ground" }
    ],
    code: `"""
Practical 3_4: Button Controlled LED.
Uses event callbacks to toggle the LED synchronously with button presses.
"""
from signal import pause
from nielit_rpi.gpio import LEDController, ButtonReader

LED_PIN = 17
BUTTON_PIN = 27

def main() -> None:
    print("Practical 3_4: Press button on GPIO 27 to light LED on GPIO 17.")
    led = LEDController(pin=LED_PIN)
    button = ButtonReader(pin=BUTTON_PIN, pull_up=True)
    
    button.when_pressed = lambda: (led.on(), print("Event: Button Pressed -> LED ON"))
    button.when_released = lambda: (led.off(), print("Event: Button Released -> LED OFF"))
    
    try:
        pause()
    except KeyboardInterrupt:
        print("\\nTerminating application.")
    finally:
        led.close()
        button.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_4",
    expectedOutput: `Practical 3_4: Press button on GPIO 27 to light LED on GPIO 17.
Event: Button Pressed -> LED ON
Event: Button Released -> LED OFF`,
    troubleshooting: [
      "LED doesn't respond: Test button and LED independently with practicals 3.2 and 3.3.",
      "LED remains lit: Check if button is stuck or wired across connected breadboard pins."
    ],
    safetyNotes: "Verify both GPIO pins (17 and 27) are configured with correct mode before running."
  },
  {
    id: "3_5",
    num: "3.5",
    title: "Traffic Light Sequencer",
    category: "Actuators",
    difficulty: "Beginner",
    hardware: "3x LEDs (Red, Yellow, Green) + Resistors",
    pins: [17, 27, 22],
    protocols: ["Multi-Pin Digital Sequencer"],
    dependencies: ["gpiozero"],
    aim: "Simulate a real-world automated traffic light sequence (Red -> Green -> Yellow -> Red) using timed states.",
    objectives: [
      "Control multiple GPIO pins concurrently",
      "Implement finite state machine timing for traffic systems",
      "Manage sequential resource allocation and cleanup"
    ],
    components: [
      "Raspberry Pi",
      "1x Red LED, 1x Yellow LED, 1x Green LED",
      "3x 330Ω Resistors",
      "Breadboard and Jumper Wires"
    ],
    wiring: [
      { component: "Red LED Anode", pin: "GPIO 17 (Pin 11)", note: "Via 330Ω resistor" },
      { component: "Yellow LED Anode", pin: "GPIO 27 (Pin 13)", note: "Via 330Ω resistor" },
      { component: "Green LED Anode", pin: "GPIO 22 (Pin 15)", note: "Via 330Ω resistor" },
      { component: "All Cathodes", pin: "GND (Pin 6/9/14/20)", note: "Shared ground rail on breadboard" }
    ],
    code: `"""
Practical 3_5: Traffic Light Controller.
Executes an automated Red-Green-Yellow traffic light cycle.
"""
import time
from nielit_rpi.gpio import LEDController
from nielit_rpi.utilities import cleanup_devices

RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

def main() -> None:
    red = LEDController(pin=RED_PIN)
    yellow = LEDController(pin=YELLOW_PIN)
    green = LEDController(pin=GREEN_PIN)
    
    print("Traffic Light Sequence running. Press Ctrl+C to stop.")
    try:
        while True:
            # RED Phase (Stop)
            print("[STOP]  RED ON (5s)")
            red.on(); yellow.off(); green.off()
            time.sleep(5)
            
            # GREEN Phase (Go)
            print("[GO]    GREEN ON (5s)")
            red.off(); yellow.off(); green.on()
            time.sleep(5)
            
            # YELLOW Phase (Caution)
            print("[WARN]  YELLOW ON (2s)")
            red.off(); yellow.on(); green.off()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\\nStopping traffic light.")
    finally:
        cleanup_devices(red, yellow, green)
        print("All lights OFF and pins cleaned.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_5",
    expectedOutput: `Traffic Light Sequence running. Press Ctrl+C to stop.
[STOP]  RED ON (5s)
[GO]    GREEN ON (5s)
[WARN]  YELLOW ON (2s)
^C
Stopping traffic light.
All lights OFF and pins cleaned.`,
    troubleshooting: [
      "Wrong color illuminates: Verify pin assignments (17=Red, 27=Yellow, 22=Green).",
      "Flickering lights: Check for loose jumper wires on the breadboard common ground."
    ],
    safetyNotes: "Ensure each LED has its own individual resistor. Never parallel LEDs on a single resistor."
  },
  {
    id: "3_6",
    num: "3.6",
    title: "PWM LED Brightness & Breathing Effect",
    category: "GPIO",
    difficulty: "Beginner",
    hardware: "LED + Resistor",
    pins: [18],
    protocols: ["Hardware / Software PWM"],
    dependencies: ["gpiozero"],
    aim: "Control analog LED intensity and generate smooth breathing fade effects using Pulse Width Modulation (PWM).",
    objectives: [
      "Understand PWM principles: Duty Cycle and Frequency",
      "Differentiate between discrete digital states and perceived analog brightness",
      "Implement linear duty cycle incrementing in Python",
      "Utilize hardware PWM-capable pins (GPIO 18 / PWM0)"
    ],
    components: [
      "Raspberry Pi",
      "5mm LED",
      "330Ω Resistor",
      "Breadboard and Wires"
    ],
    wiring: [
      { component: "LED Anode (+)", pin: "GPIO 18 (Pin 12 - PWM0)", note: "Via 330Ω resistor" },
      { component: "LED Cathode (-)", pin: "GND (Pin 14)", note: "To Ground" }
    ],
    code: `"""
Practical 3_6: PWM LED Brightness Control.
Demonstrates smooth duty cycle transitions from 0% to 100% and back.
"""
import time
from nielit_rpi.gpio import PWMLEDController

PWM_PIN = 18
CYCLES = 3

def main() -> None:
    print(f"Starting PWM Brightness fade on GPIO {PWM_PIN}.")
    led = PWMLEDController(pin=PWM_PIN, frequency=100)
    
    try:
        for cycle in range(1, CYCLES + 1):
            print(f"--- Cycle {cycle}/{CYCLES} ---")
            
            # Fade In: 0% -> 100%
            for duty in range(0, 101, 5):
                led.value = duty / 100.0
                time.sleep(0.04)
                
            # Fade Out: 100% -> 0%
            for duty in range(100, -1, -5):
                led.value = duty / 100.0
                time.sleep(0.04)
                
        print("PWM demonstration completed.")
    except KeyboardInterrupt:
        print("\\nStopped.")
    finally:
        led.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_6",
    expectedOutput: `Starting PWM Brightness fade on GPIO 18.
--- Cycle 1/3 ---
--- Cycle 2/3 ---
--- Cycle 3/3 ---
PWM demonstration completed.`,
    troubleshooting: [
      "Visible flickering: Ensure PWM frequency is >= 100Hz so persistence of vision smooths light output.",
      "LED stays full bright: Verify gpiozero is properly controlling duty cycle."
    ],
    safetyNotes: "GPIO 18 supports hardware PWM which delivers jitter-free timing compared to software-emulated PWM."
  },
  {
    id: "3_7",
    num: "3.7",
    title: "Active Buzzer Alert Sounder",
    category: "Actuators",
    difficulty: "Beginner",
    hardware: "5V/3.3V Active Buzzer Module",
    pins: [23],
    protocols: ["Digital Output"],
    dependencies: ["gpiozero"],
    aim: "Interface an active buzzer module to generate audible alarm and notification beep patterns.",
    objectives: [
      "Distinguish between Active buzzers (internal oscillator) and Passive buzzers",
      "Drive an active buzzer using digital switching logic",
      "Create cadence alert patterns for emergency indicators"
    ],
    components: [
      "Raspberry Pi",
      "Active Buzzer Module (3.3V/5V compatible with transistor driver)",
      "Breadboard and Wires"
    ],
    wiring: [
      { component: "Buzzer Signal / (+)", pin: "GPIO 23 (Pin 16)", note: "Direct signal pin" },
      { component: "Buzzer GND / (-)", pin: "GND (Pin 20)", note: "Ground rail" },
      { component: "Buzzer VCC (if 3-pin module)", pin: "3.3V (Pin 1) or 5V (Pin 2)", note: "Check module voltage rating" }
    ],
    code: `"""
Practical 3_7: Buzzer Alert System.
Sounds pulsed acoustic alert patterns.
"""
import time
from nielit_rpi.gpio import BuzzerController

BUZZER_PIN = 23

def main() -> None:
    print(f"Starting Buzzer Alert on GPIO {BUZZER_PIN}.")
    buzzer = BuzzerController(pin=BUZZER_PIN)
    
    try:
        for i in range(5):
            print(f"Beep {i+1}/5")
            buzzer.on()
            time.sleep(0.2)
            buzzer.off()
            time.sleep(0.2)
        print("Alert pattern complete.")
    except KeyboardInterrupt:
        print("\\nSilencing buzzer.")
    finally:
        buzzer.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_7",
    expectedOutput: `Starting Buzzer Alert on GPIO 23.
Beep 1/5
Beep 2/5
Beep 3/5
Beep 4/5
Beep 5/5
Alert pattern complete.`,
    troubleshooting: [
      "Clicking without sound: You may have a passive buzzer requiring an AC square wave, or voltage is too low.",
      "Continuous screeching: Check if module is Active LOW (inverts high/low logic)."
    ],
    safetyNotes: "Direct coil electromagnetic buzzers can produce back-EMF spikes. Use module boards that include protection diodes."
  },
  {
    id: "3_8",
    num: "3.8",
    title: "Servo Motor Angular Positioning",
    category: "Actuators",
    difficulty: "Intermediate",
    hardware: "SG90 Micro Servo Motor + External Power",
    pins: [18],
    protocols: ["PWM Pulse-Width Positioning (50Hz / 20ms)"],
    dependencies: ["gpiozero"],
    aim: "Control angular position of an SG90 servo motor from -90° to +90° using precision PWM pulse widths.",
    objectives: [
      "Understand RC servo timing (1ms = -90°, 1.5ms = 0°, 2ms = +90° at 50Hz)",
      "Learn power isolation requirements between digital logic and inductive motor loads",
      "Command discrete angles and programmatic angle sweeps"
    ],
    components: [
      "Raspberry Pi",
      "SG90 Micro Servo 9g",
      "External 5V 1A–2A Power Supply / Battery Pack",
      "Common Ground Jumper Wire"
    ],
    wiring: [
      { component: "Servo PWM Signal (Orange/Yellow)", pin: "GPIO 18 (Pin 12)", note: "Direct to Raspberry Pi PWM0 pin" },
      { component: "Servo Power (Red VCC)", pin: "External 5V Power (+)", note: "DO NOT power from Raspberry Pi 3.3V/5V header" },
      { component: "Servo Ground (Brown/Black)", pin: "External Power (-) & RPi GND (Pin 6)", note: "Must share Common Ground!" }
    ],
    code: `"""
Practical 3_8: Servo Motor Control.
Positions an SG90 servo through sequential angle steps from -90 to +90 deg.
"""
import time
from nielit_rpi.actuators import ServoController

SERVO_PIN = 18

def main() -> None:
    print(f"Initializing Servo on GPIO {SERVO_PIN}. Ensure external 5V power is connected.")
    servo = ServoController(
        pin=SERVO_PIN,
        min_angle=-90,
        max_angle=90,
        min_pulse_width=0.0005,
        max_pulse_width=0.0025
    )
    
    angles = [-90, -45, 0, 45, 90, 45, 0, -45, -90]
    try:
        for angle in angles:
            print(f"Setting Servo Angle: {angle:+3d}°")
            servo.angle = angle
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\\nServo movement halted.")
    finally:
        servo.detach()
        servo.close()
        print("Servo detached and PWM stopped.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_8",
    expectedOutput: `Initializing Servo on GPIO 18. Ensure external 5V power is connected.
Setting Servo Angle: -90°
Setting Servo Angle: -45°
Setting Servo Angle:  +0°
Setting Servo Angle: +45°
Setting Servo Angle: +90°
...
Servo detached and PWM stopped.`,
    troubleshooting: [
      "Raspberry Pi reboots when servo moves: Servo is drawing peak stall current from RPi power rail; switch to external 5V supply.",
      "Servo twitches / jitters: Ensure External Power GND and Raspberry Pi GND are firmly connected together.",
      "Limited movement range: Adjust min_pulse_width (0.5ms) and max_pulse_width (2.5ms) to match your specific servo model."
    ],
    safetyNotes: "NEVER power a servo motor directly from the Raspberry Pi 3.3V pin. Large inductive surge currents can reset or damage the Pi."
  },
  {
    id: "3_9",
    num: "3.9",
    title: "Ultrasonic Distance Measurement (HC-SR04)",
    category: "Sensors",
    difficulty: "Intermediate",
    hardware: "HC-SR04 Sensor + Voltage Divider",
    pins: [23, 24],
    protocols: ["Ultrasonic Time-of-Flight (343 m/s)"],
    dependencies: ["gpiozero"],
    aim: "Measure physical distance to an obstacle using an HC-SR04 ultrasonic transceiver and voltage divider circuit.",
    objectives: [
      "Understand Ultrasonic Time-of-Flight (ToF) distance calculation: Distance = (Time × Speed of Sound) / 2",
      "Construct a resistor voltage divider (1kΩ / 2kΩ) to protect 3.3V GPIO from 5V Echo pulses",
      "Filter sensor noise and manage out-of-range timeout scenarios"
    ],
    components: [
      "Raspberry Pi",
      "HC-SR04 Ultrasonic Distance Sensor",
      "1kΩ and 2kΩ Resistors (for 5V -> 3.3V Echo divider)",
      "Breadboard and Wires"
    ],
    wiring: [
      { component: "HC-SR04 VCC", pin: "5V (Pin 2 or Pin 4)", note: "Sensor requires 5V operating voltage" },
      { component: "HC-SR04 GND", pin: "GND (Pin 6)", note: "Ground reference" },
      { component: "HC-SR04 Trig", pin: "GPIO 23 (Pin 16)", note: "Output trigger pulse (3.3V is sufficient)" },
      { component: "HC-SR04 Echo", pin: "GPIO 24 (Pin 18) via Divider", note: "CRITICAL: Connect through 1kΩ/2kΩ divider to step 5V down to 3.3V!" }
    ],
    code: `"""
Practical 3_9: HC-SR04 Distance Measurement.
Measures obstacle distance in centimeters in continuous sampling loop.
"""
import time
from nielit_rpi.sensors import UltrasonicSensor

TRIG_PIN = 23
ECHO_PIN = 24

def main() -> None:
    print(f"HC-SR04 Distance Monitor (TRIG: GPIO {TRIG_PIN}, ECHO: GPIO {ECHO_PIN})")
    sensor = UltrasonicSensor(trigger_pin=TRIG_PIN, echo_pin=ECHO_PIN, max_distance=4.0)
    
    try:
        while True:
            dist_cm = sensor.distance_cm
            print(f"Measured Distance: {dist_cm:6.1f} cm", end="\\r", flush=True)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\\nStopping measurement.")
    finally:
        sensor.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_9",
    expectedOutput: `HC-SR04 Distance Monitor (TRIG: GPIO 23, ECHO: GPIO 24)
Measured Distance:   42.3 cm
Measured Distance:   35.8 cm
Measured Distance:   18.1 cm`,
    troubleshooting: [
      "Readings return max 400cm / timeout: Check echo voltage divider wiring and ensure obstacle is flat & within 2cm–400cm.",
      "Zero distance returned: Check Trig and Echo pin swapping."
    ],
    safetyNotes: "WARNING: HC-SR04 Echo pin outputs 5V. Connecting 5V directly to a Raspberry Pi GPIO pin will PERMANENTLY DESTROY the GPIO port. Always use a voltage divider."
  },
  {
    id: "3_10",
    num: "3.10",
    title: "DHT11 Temperature & Humidity Sensor",
    category: "Sensors",
    difficulty: "Intermediate",
    hardware: "DHT11 Digital Sensor",
    pins: [4],
    protocols: ["Proprietary Single-Wire Digital Bus"],
    dependencies: ["adafruit-circuitpython-dht", "adafruit-blinka"],
    aim: "Acquire ambient room temperature (°C) and relative humidity (%) readings using a digital DHT11 sensor.",
    objectives: [
      "Understand single-bus bidirectional data framing and checksum verification",
      "Handle timing-sensitive signal read retries gracefully in Python",
      "Format and display environmental metrics for telemetry"
    ],
    components: [
      "Raspberry Pi",
      "DHT11 (or DHT22/AM2302) Sensor Module",
      "4.7kΩ–10kΩ Pull-Up Resistor (if using 4-pin raw sensor)",
      "Breadboard and Wires"
    ],
    wiring: [
      { component: "DHT11 VCC", pin: "3.3V (Pin 1)", note: "Can operate on 3.3V or 5V (3.3V recommended)" },
      { component: "DHT11 GND", pin: "GND (Pin 9)", note: "Ground" },
      { component: "DHT11 Data", pin: "GPIO 4 (Pin 7)", note: "Data line with 10k pull-up resistor to 3.3V" }
    ],
    code: `"""
Practical 3_10: DHT11 Temperature and Humidity Sensor.
Reads climate data with automatic checksum retry handling.
"""
import time
import board
from nielit_rpi.sensors import DHTSensor

def main() -> None:
    print("Initializing DHT11 Sensor on GPIO 4 (board.D4)...")
    sensor = DHTSensor(pin=board.D4, sensor_type="DHT11")
    
    try:
        while True:
            temp, hum = sensor.read()
            if temp is not None and hum is not None:
                print(f"Temperature: {temp:5.1f} °C  |  Humidity: {hum:5.1f} %")
            else:
                print("Reading retry...")
            time.sleep(2.0)
    except KeyboardInterrupt:
        print("\\nExiting DHT monitor.")
    finally:
        sensor.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_10",
    expectedOutput: `Initializing DHT11 Sensor on GPIO 4 (board.D4)...
Temperature:  26.4 °C  |  Humidity:  58.0 %
Temperature:  26.5 °C  |  Humidity:  58.2 %
Temperature:  26.4 °C  |  Humidity:  57.9 %`,
    troubleshooting: [
      "Frequent checksum / RuntimeError errors: DHT11 single-wire protocol is timing-sensitive; retrying every 2s is standard behavior.",
      "No data returned: Verify pull-up resistor (4.7k–10k) is present between VCC and Data pin."
    ],
    safetyNotes: "Minimum sampling period for DHT11 is 1 second (recommended 2s). Do not query faster to prevent sensor self-heating."
  },
  {
    id: "3_11",
    num: "3.11",
    title: "I2C 16x2 Character LCD Display",
    category: "Displays",
    difficulty: "Intermediate",
    hardware: "16x2 Character LCD + PCF8574 I2C Backpack",
    pins: [2, 3],
    protocols: ["I2C Bus (0x27 / 0x3F Address)"],
    dependencies: ["smbus2"],
    aim: "Display formatted alpha-numeric text strings on a 16x2 character LCD via I2C serial interface.",
    objectives: [
      "Understand I2C master-slave communication architecture (SDA / SCL lines)",
      "Enable and scan the Raspberry Pi I2C peripheral bus using i2cdetect",
      "Control PCF8574 8-bit I/O expander to drive HD44780 LCD in 4-bit nibble mode"
    ],
    components: [
      "Raspberry Pi",
      "16x2 LCD with PCF8574T/AT I2C Backpack module",
      "Female-to-Female Jumper Wires"
    ],
    wiring: [
      { component: "LCD VCC", pin: "5V (Pin 2)", note: "LCD backlight requires 5V" },
      { component: "LCD GND", pin: "GND (Pin 6)", note: "Ground" },
      { component: "LCD SDA", pin: "GPIO 2 (Pin 3 - SDA1)", note: "I2C Serial Data" },
      { component: "LCD SCL", pin: "GPIO 3 (Pin 5 - SCL1)", note: "I2C Serial Clock" }
    ],
    code: `"""
Practical 3_11: I2C LCD Display (16x2).
Writes two lines of status text to an HD44780 LCD via PCF8574 backpack.
"""
import time
from nielit_rpi.displays import I2CLCD

LCD_I2C_ADDR = 0x27

def main() -> None:
    print(f"Initializing 16x2 I2C LCD at address 0x{LCD_I2C_ADDR:02X}...")
    lcd = I2CLCD(address=LCD_I2C_ADDR, bus_number=1)
    
    try:
        lcd.clear()
        lcd.write_string("NIELIT Raspberry", line=1)
        lcd.write_string("I2C LCD Practical", line=2)
        print("Text sent to LCD. Displaying for 5 seconds...")
        time.sleep(5.0)
    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear()
        lcd.close()
        print("LCD cleared and I2C bus closed.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_11",
    expectedOutput: `Initializing 16x2 I2C LCD at address 0x27...
Text sent to LCD. Displaying for 5 seconds...
LCD cleared and I2C bus closed.`,
    troubleshooting: [
      "Display shows solid black boxes: Adjust the blue potentiometer on the back of the I2C backpack to set contrast.",
      "Address error: Run 'i2cdetect -y 1' in terminal to confirm if module is at 0x27 or 0x3F.",
      "I2C interface disabled: Enable I2C using 'sudo raspi-config' -> Interface Options -> I2C."
    ],
    safetyNotes: "I2C lines (SDA/SCL) have internal pull-ups to 3.3V on the Raspberry Pi board. Most PCF8574 modules are safe on 5V supply because they pull lines down only."
  },
  {
    id: "3_12",
    num: "3.12",
    title: "PIR Motion Detection & Security Alarm",
    category: "Sensors",
    difficulty: "Intermediate",
    hardware: "HC-SR501 PIR Motion Sensor",
    pins: [4],
    protocols: ["Digital Input (Active HIGH)"],
    dependencies: ["gpiozero"],
    aim: "Detect human or animal infrared motion signatures using a Pyroelectric Infrared (PIR) sensor.",
    objectives: [
      "Understand Fresnel lens optics and dual-element infrared PIR detection",
      "Calibrate sensor sensitivity and trigger delay potentiometers",
      "Process motion enter/exit events asynchronously"
    ],
    components: [
      "Raspberry Pi",
      "HC-SR501 PIR Motion Sensor Module",
      "Jumper Wires"
    ],
    wiring: [
      { component: "PIR VCC", pin: "5V (Pin 2)", note: "HC-SR501 on-board regulator requires 5V" },
      { component: "PIR GND", pin: "GND (Pin 6)", note: "Ground" },
      { component: "PIR OUT", pin: "GPIO 4 (Pin 7)", note: "Outputs 3.3V logic (safe for RPi)" }
    ],
    code: `"""
Practical 3_12: PIR Motion Detection.
Monitors infrared motion with event callbacks.
"""
from signal import pause
from nielit_rpi.sensors import PIRSensor

PIR_PIN = 4

def main() -> None:
    print(f"Initializing PIR Motion Sensor on GPIO {PIR_PIN}...")
    pir = PIRSensor(pin=PIR_PIN)
    
    pir.when_motion = lambda: print(">>> ALERT: Motion Detected! <<<")
    pir.when_no_motion = lambda: print("--- Area Clear: No Motion ---")
    
    print("PIR Sensor Active. Monitoring space (Press Ctrl+C to stop)...")
    try:
        pause()
    except KeyboardInterrupt:
        print("\\nStopping PIR monitor.")
    finally:
        pir.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_12",
    expectedOutput: `Initializing PIR Motion Sensor on GPIO 4...
PIR Sensor Active. Monitoring space (Press Ctrl+C to stop)...
>>> ALERT: Motion Detected! <<<
--- Area Clear: No Motion ---
>>> ALERT: Motion Detected! <<<`,
    troubleshooting: [
      "False triggers during first 60 seconds: PIR sensors require 30–60 seconds warmup stabilization time.",
      "Trigger stays HIGH continuously: Turn the time-delay potentiometer counter-clockwise to reduce hold time to minimum (approx 3s)."
    ],
    safetyNotes: "Ensure jumper on HC-SR501 is set to 'H' (repeatable trigger mode) for continuous occupancy detection."
  },
  {
    id: "3_13",
    num: "3.13",
    title: "5V Relay Module High-Power Switching",
    category: "Actuators",
    difficulty: "Intermediate",
    hardware: "3.3V-Triggered 5V Relay Module",
    pins: [17],
    protocols: ["Digital Output (Isolated Optical/Electromechanical)"],
    dependencies: ["gpiozero"],
    aim: "Switch high-current / external loads safely using an optocoupler-isolated relay module.",
    objectives: [
      "Understand electromechanical relay contact mechanics: Common (COM), Normally Open (NO), Normally Closed (NC)",
      "Learn optical isolation principles separating digital electronics from high-power loads",
      "Control relay state safely via Python context managers"
    ],
    components: [
      "Raspberry Pi",
      "5V 1-Channel Relay Module (Active High with Optocoupler)",
      "External DC Load (e.g. 12V LED Strip, DC Fan)",
      "External Power Supply for the Load"
    ],
    wiring: [
      { component: "Relay Module VCC", pin: "5V (Pin 2)", note: "Relay coil power" },
      { component: "Relay Module GND", pin: "GND (Pin 6)", note: "Ground" },
      { component: "Relay Module IN", pin: "GPIO 17 (Pin 11)", note: "Digital control signal" },
      { component: "Relay Output COM & NO", pin: "External Circuit Switch", note: "Acts as a mechanical switch in series with external load" }
    ],
    code: `"""
Practical 3_13: Relay Control.
Controls a relay module to switch an external electrical load.
"""
import time
from nielit_rpi.actuators import RelayController

RELAY_PIN = 17

def main() -> None:
    print(f"Initializing Relay Controller on GPIO {RELAY_PIN}...")
    relay = RelayController(pin=RELAY_PIN, active_high=True)
    
    try:
        print("Relay: Switching ON (Contact COM -> NO Closed)...")
        relay.on()
        time.sleep(3.0)
        
        print("Relay: Switching OFF (Contact COM -> NO Open)...")
        relay.off()
        time.sleep(1.0)
    except KeyboardInterrupt:
        print("\\nInterrupted.")
    finally:
        relay.off()
        relay.close()
        print("Relay safely returned to OFF state.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_13",
    expectedOutput: `Initializing Relay Controller on GPIO 17...
Relay: Switching ON (Contact COM -> NO Closed)...
Relay: Switching OFF (Contact COM -> NO Open)...
Relay safely returned to OFF state.`,
    troubleshooting: [
      "LED on relay lights up but no audible 'click': 5V power supply to relay coil is insufficient.",
      "Inverted operation: If relay turns ON when pin is LOW, set active_high=False."
    ],
    safetyNotes: "DANGER / HIGH VOLTAGE WARNING: In student laboratories, ONLY connect low-voltage DC loads (5V–24V DC). NEVER connect 110V/230V AC mains electricity without certified industrial enclosures and qualified supervision."
  },
  {
    id: "3_14",
    num: "3.14",
    title: "Analog Sensor Reading - LDR with MCP3008 ADC",
    category: "Sensors",
    difficulty: "Intermediate",
    hardware: "MCP3008 8-Channel 10-Bit SPI ADC + LDR",
    pins: [8, 9, 10, 11],
    protocols: ["SPI Serial Peripheral Interface (Bus 0)"],
    dependencies: ["gpiozero", "spidev"],
    aim: "Read continuous analog voltage signals from a Light Dependent Resistor (LDR) using the MCP3008 SPI Analog-to-Digital Converter.",
    objectives: [
      "Understand why Raspberry Pi requires an external ADC (Raspberry Pi GPIO is strictly digital)",
      "Learn SPI 4-wire bus signals: MOSI, MISO, SCLK, and CE0 (Chip Enable)",
      "Convert 10-bit digital values (0–1023) into normalized ratios and voltage equivalents (0V–3.3V)"
    ],
    components: [
      "Raspberry Pi",
      "MCP3008 8-Channel 10-bit ADC IC",
      "LDR (Photoresistor)",
      "10kΩ Fixed Resistor (Voltage Divider)",
      "Breadboard and Wires"
    ],
    wiring: [
      { component: "MCP3008 VDD & VREF", pin: "3.3V (Pin 1)", note: "Power and ADC reference voltage" },
      { component: "MCP3008 AGND & DGND", pin: "GND (Pin 6)", note: "Analog and Digital Ground" },
      { component: "MCP3008 CLK", pin: "GPIO 11 (Pin 23 - SCLK)", note: "SPI Clock" },
      { component: "MCP3008 DOUT", pin: "GPIO 9 (Pin 21 - MISO)", note: "SPI Master-In Slave-Out" },
      { component: "MCP3008 DIN", pin: "GPIO 10 (Pin 19 - MOSI)", note: "SPI Master-Out Slave-In" },
      { component: "MCP3008 CS/SHDN", pin: "GPIO 8 (Pin 24 - CE0)", note: "Chip Select 0" },
      { component: "MCP3008 CH0 (Pin 1)", pin: "LDR Divider Junction", note: "LDR connected to 3.3V, 10k resistor to GND" }
    ],
    code: `"""
Practical 3_14: LDR + MCP3008 ADC.
Reads analog light level via SPI Channel 0.
"""
import time
from nielit_rpi.sensors import LDRSensor

ADC_CHANNEL = 0

def main() -> None:
    print(f"Monitoring LDR Ambient Light on MCP3008 Channel {ADC_CHANNEL}...")
    ldr = LDRSensor(channel=ADC_CHANNEL)
    
    try:
        while True:
            intensity = ldr.value
            voltage = ldr.voltage
            print(f"Light Intensity: {intensity * 100:5.1f}%  |  Voltage: {voltage:5.3f} V", end="\\r", flush=True)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\\nStopped ADC monitor.")
    finally:
        ldr.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_14",
    expectedOutput: `Monitoring LDR Ambient Light on MCP3008 Channel 0...
Light Intensity:  78.4%  |  Voltage: 2.587 V
Light Intensity:  21.2%  |  Voltage: 0.700 V (covered LDR)
Light Intensity:  85.6%  |  Voltage: 2.825 V`,
    troubleshooting: [
      "Error 'No SPI device': Enable SPI interface via 'sudo raspi-config' -> Interface Options -> SPI.",
      "Reading stays 0.00V: Check MCP3008 power pins (Pin 16 VDD and Pin 15 VREF must connect to 3.3V)."
    ],
    safetyNotes: "MCP3008 VREF must not exceed 3.3V when connected to Raspberry Pi to prevent MISO logic level damage."
  },
  {
    id: "3_15",
    num: "3.15",
    title: "MFRC522 RFID Card & Keyfob Reader",
    category: "Communication",
    difficulty: "Advanced",
    hardware: "MFRC522 RFID Module (13.56 MHz) + MIFARE Card",
    pins: [8, 9, 10, 11, 25],
    protocols: ["SPI Bus + 13.56 MHz RFID/NFC (ISO 14443A)"],
    dependencies: ["mfrc522", "spidev"],
    aim: "Read unique identifiers (UID) and sector text payload from 13.56 MHz MIFARE RFID cards and key fobs.",
    objectives: [
      "Understand RFID tag resonance, antenna coupling, and anti-collision protocols",
      "Interact with RC522 transceiver IC over SPI bus",
      "Authenticate and read data blocks from MIFARE Classic 1K tags"
    ],
    components: [
      "Raspberry Pi",
      "RC522 13.56 MHz RFID Reader Module",
      "MIFARE Classic 1K RFID Card and Keyfob",
      "Jumper Wires"
    ],
    wiring: [
      { component: "RC522 3.3V (VCC)", pin: "3.3V (Pin 1)", note: "DO NOT CONNECT TO 5V!" },
      { component: "RC522 RST", pin: "GPIO 25 (Pin 22)", note: "Module Reset line" },
      { component: "RC522 GND", pin: "GND (Pin 6)", note: "Ground" },
      { component: "RC522 MISO", pin: "GPIO 9 (Pin 21 - MISO)", note: "SPI Data In" },
      { component: "RC522 MOSI", pin: "GPIO 10 (Pin 19 - MOSI)", note: "SPI Data Out" },
      { component: "RC522 SCK", pin: "GPIO 11 (Pin 23 - SCLK)", note: "SPI Clock" },
      { component: "RC522 SDA (NSS)", pin: "GPIO 8 (Pin 24 - CE0)", note: "SPI Chip Select 0" }
    ],
    code: `"""
Practical 3_15: MFRC522 RFID Read/Write.
Reads UID and text from MIFARE RFID cards.
"""
from nielit_rpi.communication import RFIDReader

def main() -> None:
    print("MFRC522 RFID Reader Ready.")
    print("Please hold an RFID card or keyfob near the reader...")
    reader = RFIDReader()
    
    try:
        card_id, text = reader.read()
        print("=" * 40)
        print(f"Card Detected!")
        print(f"Unique ID (UID) : {card_id}")
        print(f"Stored Text     : {text.strip()}")
        print("=" * 40)
    except KeyboardInterrupt:
        print("\\nRFID scan canceled.")
    finally:
        reader.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_15",
    expectedOutput: `MFRC522 RFID Reader Ready.
Please hold an RFID card or keyfob near the reader...
========================================
Card Detected!
Unique ID (UID) : 832941058291
Stored Text     : NIELIT STUDENT 001
========================================`,
    troubleshooting: [
      "Module not detecting cards: Ensure RC522 VCC is powered by 3.3V pin and SPI is enabled in raspi-config.",
      "Reader hangs: Recheck SDA/CE0 connection on Pin 24."
    ],
    safetyNotes: "MFRC522 IC is strictly a 3.3V chip. Connecting VCC to 5V will burn the RF frontend."
  },
  {
    id: "3_16",
    num: "3.16",
    title: "SQLite Sensor Telemetry Logger",
    category: "Storage",
    difficulty: "Intermediate",
    hardware: "Raspberry Pi Local Storage",
    pins: [],
    protocols: ["SQLite Embedded Relational Database (SQL)"],
    dependencies: ["sqlite3"],
    aim: "Persist time-series sensor telemetry data into a local relational SQLite database file with structured schemas.",
    objectives: [
      "Design database schema with PRIMARY KEY, timestamp, and numeric telemetry values",
      "Execute parameterized SQL INSERT statements to prevent SQL injection vulnerabilities",
      "Query time-series historical records and calculate statistics"
    ],
    components: [
      "Raspberry Pi",
      "Local Storage (MicroSD / SSD)"
    ],
    wiring: [
      { component: "Local SQLite DB", pin: "N/A", note: "File-based storage (sensor_data.db)" }
    ],
    code: `"""
Practical 3_16: SQLite Sensor Logger.
Logs time-series readings to local SQLite database.
"""
import time
from datetime import datetime
from nielit_rpi.storage import SensorDataLogger

DB_NAME = "sensor_data.db"
TOTAL_SAMPLES = 5

def read_temperature_sim() -> float:
    # Simulated temperature reading (replace with DHTSensor in production)
    return 24.5

def main() -> None:
    print(f"Initializing SQLite Logger with database: {DB_NAME}")
    logger = SensorDataLogger(db_path=DB_NAME, table_name="readings")
    
    try:
        logger.create_table({"temperature": "REAL"})
        print(f"Logging {TOTAL_SAMPLES} consecutive readings...")
        
        for i in range(1, TOTAL_SAMPLES + 1):
            temp = read_temperature_sim() + (i * 0.2)
            logger.log_reading(temperature=round(temp, 2))
            print(f"[{i}/{TOTAL_SAMPLES}] Logged Temperature: {temp:.2f} °C")
            time.sleep(1.0)
            
        print("\\nQuerying last 5 records from database:")
        records = logger.get_readings(limit=5)
        for row in records:
            print(f"  ID: {row['id']:<3} | Time: {row['timestamp']} | Temp: {row['temperature']} °C")
    finally:
        logger.close()
        print("Database closed.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_16",
    expectedOutput: `Initializing SQLite Logger with database: sensor_data.db
Logging 5 consecutive readings...
[1/5] Logged Temperature: 24.70 °C
[2/5] Logged Temperature: 24.90 °C
[3/5] Logged Temperature: 25.10 °C
[4/5] Logged Temperature: 25.30 °C
[5/5] Logged Temperature: 25.50 °C

Querying last 5 records from database:
  ID: 5   | Time: 2026-08-11 21:50:00 | Temp: 25.5 °C
  ID: 4   | Time: 2026-08-11 21:49:59 | Temp: 25.3 °C
  ID: 3   | Time: 2026-08-11 21:49:58 | Temp: 25.1 °C
  ID: 2   | Time: 2026-08-11 21:49:57 | Temp: 24.9 °C
  ID: 1   | Time: 2026-08-11 21:49:56 | Temp: 24.7 °C
Database closed.`,
    troubleshooting: [
      "Database locked error: Always ensure SQLite connections are closed properly using context managers.",
      "Permission denied: Ensure the working directory is writable by the running user."
    ],
    safetyNotes: "Commit transactions periodically when logging continuously to prevent in-memory journal accumulation."
  },
  {
    id: "3_17",
    num: "3.17",
    title: "Flask Web Server Remote GPIO Control",
    category: "Networking",
    difficulty: "Advanced",
    hardware: "LED + Resistor + Local Area Network",
    pins: [17],
    protocols: ["HTTP / RESTful Web Framework (Port 5000)"],
    dependencies: ["flask", "gpiozero"],
    aim: "Host a lightweight Flask web application on the Raspberry Pi allowing browser-based remote GPIO switching over LAN.",
    objectives: [
      "Implement a Python micro-web server using Flask",
      "Create dynamic HTML web interface with live hardware status display",
      "Map HTTP URL route handlers (/led/on, /led/off) to physical GPIO actuators"
    ],
    components: [
      "Raspberry Pi connected to Wi-Fi / Ethernet LAN",
      "LED + 330Ω Resistor on GPIO 17",
      "Client Device (PC / Smartphone with web browser)"
    ],
    wiring: [
      { component: "LED Anode (+)", pin: "GPIO 17 (Pin 11)", note: "Via 330Ω resistor" },
      { component: "LED Cathode (-)", pin: "GND (Pin 9)", note: "Ground" }
    ],
    code: `"""
Practical 3_17: Flask GPIO Web Control.
Hosts a local web server at http://<rpi-ip>:5000 to toggle an LED.
"""
from nielit_rpi.networking import create_gpio_web_app

LED_PIN = 17
PORT = 5000

def main() -> None:
    print(f"Starting Flask GPIO Web Server on port {PORT}...")
    print(f"Open browser: http://localhost:{PORT} or http://<your-pi-ip>:{PORT}")
    
    app, led = create_gpio_web_app(led_pin=LED_PIN)
    try:
        app.run(host="0.0.0.0", port=PORT, debug=False)
    finally:
        led.close()
        print("Web server stopped and GPIO released.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_17",
    expectedOutput: `Starting Flask GPIO Web Server on port 5000...
Open browser: http://localhost:5000 or http://<your-pi-ip>:5000
 * Serving Flask app 'nielit_rpi.networking.flask_app'
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.105:5000
192.168.1.50 - - [11/Aug/2026 21:50:12] "GET / HTTP/1.1" 200 -
192.168.1.50 - - [11/Aug/2026 21:50:15] "GET /led/on HTTP/1.1" 302 -`,
    troubleshooting: [
      "Cannot access from phone: Ensure phone is connected to the SAME Wi-Fi network and use the Pi's local IP (e.g. 192.168.1.x).",
      "Port 5000 already in use: Check if another instance of Flask is running in background."
    ],
    safetyNotes: "Flask built-in server is designed for laboratory learning. For production deployment, use a WSGI server like Gunicorn behind NGINX."
  },
  {
    id: "3_18",
    num: "3.18",
    title: "MQTT IoT Telemetry Publisher",
    category: "Communication",
    difficulty: "Advanced",
    hardware: "Network Connection (Wi-Fi/Ethernet)",
    pins: [],
    protocols: ["MQTT Protocol (ISO/IEC 20922) / TCP 1883"],
    dependencies: ["paho-mqtt"],
    aim: "Publish structured JSON IoT sensor telemetry packets to a cloud/local MQTT broker over pub/sub channels.",
    objectives: [
      "Understand MQTT publish-subscribe messaging architecture vs HTTP request-response",
      "Format JSON payloads with device metadata and numerical metrics",
      "Manage MQTT Quality of Service (QoS) levels and keepalive handshakes"
    ],
    components: [
      "Raspberry Pi connected to Internet / LAN",
      "MQTT Broker (Public sandbox: test.mosquitto.org / HiveMQ)"
    ],
    wiring: [
      { component: "Network", pin: "Ethernet / Wi-Fi", note: "MQTT Broker communication" }
    ],
    code: `"""
Practical 3_18: MQTT Publisher.
Publishes structured JSON messages to MQTT broker topic.
"""
import time
from nielit_rpi.communication import MQTTPublisher

TOPIC = "nielit/rpi/sensor"

def main() -> None:
    print(f"Connecting to MQTT Broker to publish on topic: '{TOPIC}'...")
    publisher = MQTTPublisher(topic=TOPIC)
    
    try:
        publisher.connect()
        for counter in range(1, 6):
            payload = {
                "device": "raspberry-pi-lab",
                "sample_id": counter,
                "temperature": 25.5 + counter,
                "status": "OPERATIONAL"
            }
            publisher.publish(payload)
            print(f"[{counter}/5] Published packet: {payload}")
            time.sleep(2.0)
    finally:
        publisher.disconnect()
        print("MQTT Publisher disconnected.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_18",
    expectedOutput: `Connecting to MQTT Broker to publish on topic: 'nielit/rpi/sensor'...
[1/5] Published packet: {'device': 'raspberry-pi-lab', 'sample_id': 1, 'temperature': 26.5, 'status': 'OPERATIONAL'}
[2/5] Published packet: {'device': 'raspberry-pi-lab', 'sample_id': 2, 'temperature': 27.5, 'status': 'OPERATIONAL'}
[3/5] Published packet: {'device': 'raspberry-pi-lab', 'sample_id': 3, 'temperature': 28.5, 'status': 'OPERATIONAL'}
...
MQTT Publisher disconnected.`,
    troubleshooting: [
      "Broker connection failed: Verify Internet connectivity and check if port 1883 is unblocked on your network.",
      "Custom Broker: Override via environment variable 'export MQTT_BROKER=your.broker.com'."
    ],
    safetyNotes: "Public brokers (e.g. test.mosquitto.org) are open to the world. Never publish sensitive private data on public test topics."
  },
  {
    id: "3_19",
    num: "3.19",
    title: "MQTT Subscriber Remote Actuation",
    category: "Communication",
    difficulty: "Advanced",
    hardware: "LED + Resistor + Network",
    pins: [17],
    protocols: ["MQTT Protocol (Callback API v2)"],
    dependencies: ["paho-mqtt", "gpiozero"],
    aim: "Subscribe to cloud MQTT control topics and trigger real-time physical GPIO actuators based on incoming message payloads.",
    objectives: [
      "Implement asynchronous MQTT message reception handlers (on_message)",
      "Parse command payloads ('ON' / 'OFF') safely",
      "Actuate GPIO hardware in real time from remote cloud triggers"
    ],
    components: [
      "Raspberry Pi with Internet Connection",
      "LED + 330Ω Resistor on GPIO 17"
    ],
    wiring: [
      { component: "LED Anode (+)", pin: "GPIO 17 (Pin 11)", note: "Via 330Ω resistor" },
      { component: "LED Cathode (-)", pin: "GND (Pin 9)", note: "Ground" }
    ],
    code: `"""
Practical 3_19: MQTT Subscriber + GPIO.
Receives cloud MQTT commands to switch physical LED on/off.
"""
from nielit_rpi.gpio import LEDController
from nielit_rpi.communication import MQTTSubscriber

LED_PIN = 17
TOPIC = "nielit/rpi/led"

def main() -> None:
    led = LEDController(pin=LED_PIN)
    
    def on_command_received(command: str) -> None:
        cmd = command.strip().lower()
        print(f"Received Cloud Command: '{cmd}'")
        if cmd == "on":
            led.on()
            print(">>> Physical Action: LED ON <<<")
        elif cmd == "off":
            led.off()
            print(">>> Physical Action: LED OFF <<<")
        else:
            print(f"Ignored unknown command: {command}")
            
    subscriber = MQTTSubscriber(topic=TOPIC, on_message_callback=on_command_received)
    print(f"Subscribed to topic '{TOPIC}'. Waiting for incoming commands...")
    
    try:
        subscriber.connect()
        subscriber.start()
    except KeyboardInterrupt:
        print("\\nStopping MQTT subscriber.")
    finally:
        subscriber.stop()
        subscriber.disconnect()
        led.close()

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_19",
    expectedOutput: `Subscribed to topic 'nielit/rpi/led'. Waiting for incoming commands...
Received Cloud Command: 'on'
>>> Physical Action: LED ON <<<
Received Cloud Command: 'off'
>>> Physical Action: LED OFF <<<`,
    troubleshooting: [
      "Not receiving messages: Ensure the publisher is broadcasting to the exact same topic string ('nielit/rpi/led').",
      "Latency: Free public brokers may experience 1–2 second queuing during high load."
    ],
    safetyNotes: "Always implement sanity checks on incoming command strings before actuating physical hardware to prevent unexpected triggers."
  },
  {
    id: "3_20",
    num: "3.20",
    title: "Smart Home Automation Capstone",
    category: "System",
    difficulty: "Advanced",
    hardware: "PIR Sensor + LED/Relay + Ambient Light Logic",
    pins: [4, 17],
    protocols: ["Integrated Multi-Sensor Automation Loop"],
    dependencies: ["gpiozero"],
    aim: "Integrate presence sensing and ambient light thresholds to build an autonomous smart energy-saving illumination system.",
    objectives: [
      "Synthesize multiple sensor inputs into composite automation logic",
      "Implement energy-efficient lighting (trigger light ONLY when motion is detected AND room is dark)",
      "Build a complete end-to-end IoT edge automation application"
    ],
    components: [
      "Raspberry Pi",
      "HC-SR501 PIR Motion Sensor (GPIO 4)",
      "LED / Relay Indicator (GPIO 17)",
      "Optional LDR + MCP3008 for true analog lux sensing"
    ],
    wiring: [
      { component: "PIR Sensor OUT", pin: "GPIO 4 (Pin 7)", note: "Motion detection input" },
      { component: "PIR VCC & GND", pin: "5V (Pin 2) & GND (Pin 6)", note: "PIR power" },
      { component: "Smart Light LED/Relay", pin: "GPIO 17 (Pin 11)", note: "Actuator output" }
    ],
    code: `"""
Practical 3_20: Smart Home Automation Capstone.
Activates lighting only when human motion is detected under dark ambient conditions.
"""
import time
from nielit_rpi.gpio import LEDController
from nielit_rpi.sensors import PIRSensor

PIR_PIN = 4
LIGHT_PIN = 17
DARK_THRESHOLD = 0.35

def read_ambient_lux() -> float:
    # Returns 0.0 (pitch dark) to 1.0 (bright daylight)
    # In full hardware build, reads from LDRSensor (Practical 3.14)
    return 0.20

def main() -> None:
    print("=" * 55)
    print("   NIELIT Smart Home Energy Automation Capstone")
    print("=" * 55)
    
    pir = PIRSensor(pin=PIR_PIN)
    light = LEDController(pin=LIGHT_PIN)
    
    print("Smart Controller Active. Monitoring conditions...")
    try:
        while True:
            ambient_lux = read_ambient_lux()
            is_motion = pir.motion_detected
            
            if is_motion and ambient_lux < DARK_THRESHOLD:
                if not light.is_lit:
                    print(f"Condition: Motion [{is_motion}] & Lux [{ambient_lux:.2f} < {DARK_THRESHOLD}] -> LIGHTS ON")
                light.on()
            else:
                if light.is_lit:
                    print(f"Condition: Clear/Bright -> LIGHTS OFF")
                light.off()
                
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\\nStopping automation controller.")
    finally:
        light.off()
        light.close()
        pir.close()
        print("System shutdown cleanly.")

if __name__ == "__main__":
    main()`,
    cliCommand: "nielit-rpi run 3_20",
    expectedOutput: `=======================================================
   NIELIT Smart Home Energy Automation Capstone
=======================================================
Smart Controller Active. Monitoring conditions...
Condition: Motion [True] & Lux [0.20 < 0.35] -> LIGHTS ON
Condition: Clear/Bright -> LIGHTS OFF`,
    troubleshooting: [
      "Light never turns on: Check if ambient lux is above threshold, or PIR has timed out.",
      "Light flickers: Add a minimum on-time hysteresis delay (e.g. keep light on for at least 15 seconds after last motion)."
    ],
    safetyNotes: "Capstone project combines lessons from practicals 3.2, 3.12, 3.13, and 3.14 into an integrated IoT automation node."
  }
];

// Export if in node environment or window
if (typeof module !== 'undefined' && module.exports) {
  module.exports = PRACTICALS_DATA;
}
