from microbit import *
from machine import time_pulse_us

""" set up the ultrasonic sensor pins. The Ultrasonic sensor needs four wires to work.
in addition to power and ground, the sensor needs a trigger pin and echo pin. """
trig = pin1
echo = pin2

def setup_ultrasonic():
    """This will initialize the two pins for the ultrasonic sensor"""
    trig.write_digital(0)
    echo.read_digital()

def get_distance():
    trig.write_digital(1)
    trig.write_digital(0)

    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000

    distance_cm = (t_echo / 2) * 34300
    return distance_cm

setup_ultrasonic()

while True:
    distance = get_distance()
    print(distance)
    sleep(1000)