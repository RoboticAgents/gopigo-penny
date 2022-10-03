import time
from easygopigo3 import EasyGoPiGo3

# create the gpg object
gpg = EasyGoPiGo3()

# turn the left motor on at almost full power
gpg.set_motor_power(port=gpg.MOTOR_LEFT, power=98)
# turn the right motor on at almost full power
gpg.set_motor_power(port=gpg.MOTOR_RIGHT, power=98)
# tell the GoPiGo3 to go forward
gpg.foward()
# wait 16 seconds
time.sleep(16)
# tell the gpg to stop
gpg.stop
