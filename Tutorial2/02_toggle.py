import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button_pin = 20
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#...
toggled = False  # When button is pressed, this will flip
previous_state = False  # State of button when last checked
while True:
    state = GPIO.input(button_pin)
    if (previous_state == False and state == True):  # Button has been pressed
        toggled = not toggled  # Flip
        print(toggled)
    previous_state = state  # Update last state
    time.sleep(0.01)
#...