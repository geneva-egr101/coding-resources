#...
import gui
import RPi.GPIO as GPIO
#...
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button_pin = 20
motor_pin_1 = 13
motor_pin_2 = 14
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(motor_pin_1, GPIO.OUT)
#...
GPIO.setup(motor_pin_2, GPIO.OUT)

window = gui.create("motor_control1.ui")  # Load custom GUI from file
window.show()  # Show custom GUI as an application

toggled = False
#...
previous_state = False
while True:
    state = GPIO.input(button_pin)
    if (previous_state == False and state == True):
        toggled = not toggled
        GPIO.output(motor_pin_1, False)
        GPIO.output(motor_pin_2, toggled)
    previous_state = state
    time.sleep(0.01)