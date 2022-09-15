import time
from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()

gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=98)
gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=98)
gpg.foward()
time.sleep(20)
gpg.stop
