import gui
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button_pin = 20
motor_pin_1 = 13
motor_pin_2 = 14
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(motor_pin_1, GPIO.OUT)
GPIO.setup(motor_pin_2, GPIO.OUT)

closed = False
def on_close():
    global closed
    closed = True
    GPIO.output(motor_pin_1, False)
    GPIO.output(motor_pin_2, False)

window = gui.create("motor_control1.ui", on_close)
window.show()

#...
toggled = False
previous_state = False
while not closed:
    state = GPIO.input(button_pin)
    if (previous_state == False and state == True):
        toggled = not toggled
    if window.powerButton.isChecked():  # Should motor have power?
        if not toggled:  # Should motor turn counter-clockwise?
            GPIO.output(motor_pin_1, False)
            GPIO.output(motor_pin_2, True)
        else:  # Should motor turn clockwise?
            GPIO.output(motor_pin_1, True)
            GPIO.output(motor_pin_2, False)
    else:  # Should motor not have power?
        GPIO.output(motor_pin_1, False)
        GPIO.output(motor_pin_2, False)
    previous_state = state
    time.sleep(0.01)
#...