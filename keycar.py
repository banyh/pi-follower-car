from motor import *
import readchar
import time

car = Motor()

while True:
    key = readchar.readkey()
    if key == '\x1b[A':
        car.go(FORWARD)
        time.sleep(0.5)
        car.go(STOP)
    elif key == '\x1b[B':
        car.go(BACKWARD)
        time.sleep(0.5)
        car.go(STOP)
    elif key == '\x1b[C':
        car.go(RIGHT_FORWARD)
    elif key == '\x1b[D':
        car.go(LEFT_FORWARD)
    elif key == 'q':
        break
