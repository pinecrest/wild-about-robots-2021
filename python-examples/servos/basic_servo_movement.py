from microbit import * 
# Servo control: 
# 100 = 1 millisecond pulse all right 
# 200 = 2 millisecond pulse all left 
# 150 = 1.5 millisecond pulse center 

# Set up the servo pin. 
# You can choose pinX (where X is the 
# number next to the pin on your board)
servo_pin = pin0 
servo_pin.set_analog_period(20)
MIN_WIDTH = 0.5
MAX_WIDTH = 2.7

def move_to_angle(angle, min_angle=0, max_angle=250):
    width = (angle / max_angle) * (MAX_WIDTH - MIN_WIDTH) + MIN_WIDTH
    set_pulse(width)

def set_pulse(width):
    servo_pin.write_analog(1023 * width / 20)

while True: 
    move_to_angle(0)
    sleep(2000)
    move_to_angle(180)
    sleep(2000)