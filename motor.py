import RPi.GPIO as GPIO
import time

LEFT = 0x10
RIGHT = 0x01
FORWARD = 0x100
LEFT_FORWARD = FORWARD | LEFT
RIGHT_FORWARD = FORWARD | RIGHT
BACKWARD = 0x1000
LEFT_BACKWARD = BACKWARD | LEFT
RIGHT_BACKWARD = BACKWARD | RIGHT
STOP = 0x0000


class Motor(object):
    Motor_pin = [16, 18, 22, 24]
    Motor_speed = [0, 0, 0, 0]
    Motor_pwm = []

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        for pin in self.Motor_pin:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
            self.Motor_pwm.append(GPIO.PWM(pin, 500))
            self.Motor_pwm[-1].start(0)

    def __del__(self):
        for pwm in self.Motor_pwm:
            pwm.stop()
        pwm = []
        GPIO.cleanup()

    def setspeed(self):
        for pwm, speed in zip(self.Motor_pwm, self.Motor_speed):
            pwm.ChangeDutyCycle(speed)

    def go(self, dir, speed=70):
        if dir == STOP:
            self.Motor_speed = [0, 0, 0, 0]
        elif dir == FORWARD:
            self.Motor_speed = [speed, 0, speed, 0]
        elif dir == BACKWARD:
            self.Motor_speed = [0, speed, 0, speed]
        elif dir == LEFT_FORWARD:
            self.Motor_speed = [0, 0, speed, 0]
        elif dir == RIGHT_FORWARD:
            self.Motor_speed = [speed, 0, 0, 0]
        elif dir == LEFT_BACKWARD:
            self.Motor_speed = [0, 0, 0, speed]
        elif dir == RIGHT_BACKWARD:
            self.Motor_speed = [0, speed, 0, 0]

        self.setspeed()
