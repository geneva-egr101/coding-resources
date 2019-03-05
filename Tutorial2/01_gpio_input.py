import RPi.GPIO as GPIO  # Import module with a different name
import time
GPIO.setwarnings(False)  # Disable unnecessary warnings
GPIO.setmode(GPIO.BCM)  # Indicate numbering scheme

button_pin = 20  # Pin number as labeled on the RasPiO Pro Hat
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Default to ground

while True:
    state = GPIO.input(button_pin)  # True - 3.3V wire, False - Ground wire
    print(state)
    time.sleep(0.01)  # Wait a small amount of time to avoid bouncing