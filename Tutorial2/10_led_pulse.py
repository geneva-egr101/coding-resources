#...
import threading
import gui
#...
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button_pin = 20
motor_pin_1 = 13
motor_pin_2 = 14
led_pin = 24
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(motor_pin_1, GPIO.OUT)
GPIO.setup(motor_pin_2, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

closed = False
def on_close():
    global closed
    closed = True
    GPIO.output(motor_pin_1, False)
    GPIO.output(motor_pin_2, False)

#...
def on_power_button_click():
    threading.Thread(target=pulse_led, args=[]).start()  # When button clicked, start thread

def pulse_led():
    while window.powerButton.isChecked() and not closed:  # Stops looping if motor off or window closed
        t = window.periodSpinBox.value() / 2  # Get period in seconds; on and off for 1/2 period each
        GPIO.output(led_pin, True)
        time.sleep(t)
        GPIO.output(led_pin, False)
        time.sleep(t)

window = gui.create("motor_control3.ui", on_close)
#...
window.connect_event(window.powerButton.clicked, target=on_power_button_click, args=[])
window.show()

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
    window.update()
    time.sleep(0.01)