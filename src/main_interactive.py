import time
from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()


def triangle():
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=80)
    gpg.forward()
    time.sleep(1.5)
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=-80)
    gpg.forward()
    time.sleep(0.55)
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=80)
    gpg.forward()
    time.sleep(1.5)
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=-80)
    gpg.forward()
    time.sleep(0.38)
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=80)
    gpg.forward()
    time.sleep(1)
    gpg.stop()


def circle(final_time):
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=10)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=98)
    gpg.forward()
    time.sleep(final_time)
    gpg.stop()


def backwards_circle(final_time):
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=98)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=10)
    gpg.forward()
    time.sleep(final_time)
    gpg.stop()
