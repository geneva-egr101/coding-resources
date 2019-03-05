import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#...
button_pin = 20
motor_pin_1 = 13  # First of two pins connected to motor control chip
motor_pin_2 = 14  # Second of two pins connected to motor control chip
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(motor_pin_1, GPIO.OUT)
GPIO.setup(motor_pin_2, GPIO.OUT)

toggled = False
previous_state = False
while True:
    state = GPIO.input(button_pin)
    if (previous_state == False and state == True):
        toggled = not toggled
        GPIO.output(motor_pin_1, False)  # Always keep first motor pin off
        GPIO.output(motor_pin_2, toggled)  # Turn second motor pin on or off
    previous_state = state
    time.sleep(0.01)
#...