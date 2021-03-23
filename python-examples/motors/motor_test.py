from microbit import *

while True:
    pin0.write_analog(100)
    sleep(1000)
    pin0.write_analog(0)
    sleep(1000)