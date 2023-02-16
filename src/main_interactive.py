import time
from easygopigo3 import EasyGoPiGo3

# create go pi go instance
gpg = EasyGoPiGo3()


def triangle():
    """ Function in order to draw a triangle using go pi go """
    # set motor power and go forward
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=80)
    gpg.forward()
    time.sleep(1.5)
    # set motor power and go sideways
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=-80)
    gpg.forward()
    time.sleep(0.55)
    # set motor power and go sideways
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=80)
    gpg.forward()
    time.sleep(1.5)
    # set motor power and go sideways
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=-80)
    gpg.forward()
    time.sleep(0.38)
    # set motor power and go forwards
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=80)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=80)
    gpg.forward()
    time.sleep(1)
    # stop moving at the end of the function
    gpg.stop()


def circle(final_time):
    """ Function to draw a circle using go pi go; takes in a time variable in order to determine the sleep time"""
    # go in a circular motion for as long as the time says to
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=10)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=98)
    gpg.forward()
    time.sleep(final_time)
    gpg.stop()


def backwards_circle(final_time):
    """Function to draw a circle in the opposite direction; takes in a time variable to determine how long to run"""
    # go in a circular motion for as long as the time says to
    gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=98)
    gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=10)
    gpg.forward()
    time.sleep(final_time)
    gpg.stop()
