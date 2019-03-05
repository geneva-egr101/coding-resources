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

#...
window = gui.create("motor_control2.ui", on_close)
# When the GUI button is clicked, the program will do print("Power Button Clicked")
window.connect_event(window.powerButton.clicked, target=print, args=["powerButton clicked"])
window.show()
#...

toggled = False
previous_state = False
while not closed:
    state = GPIO.input(button_pin)
    if (previous_state == False and state == True):
        toggled = not toggled
        if toggled:
            window.directionLabel.setText("Clockwise")
        else:
            window.directionLabel.setText("Counter-Clockwise")
    if window.powerButton.isChecked():
        if not toggled:
            GPIO.output(motor_pin_1, False)
            GPIO.output(motor_pin_2, True)
        else:
            GPIO.output(motor_pin_1, True)
            GPIO.output(motor_pin_2, False)
    else:
        GPIO.output(motor_pin_1, False)
        GPIO.output(motor_pin_2, False)
    previous_state = state
    time.sleep(0.01)