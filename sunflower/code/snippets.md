Useful code snippets to copy/paste into the editor
# Photoresistors Test
This build is using four photoresistors to figure out where the Sun is located.
```
# Libraries we will need.
import board
import analogio
import time

# Assign the analog pins we are using to the four photoresistors.
pr_UR = analogio.AnalogIn(board.A3)
pr_UL = analogio.AnalogIn(board.A2)
pr_LL = analogio.AnalogIn(board.A4)
pr_LR = analogio.AnalogIn(board.A5)

# Continually loop through the values and see what we get.
while True:
    print('Upper right: {}'.format(pr_UR.value))
    print('Upper left: {}'.format(pr_UL.value))
    print('Lower right: {}'.format(pr_LR.value))
    print('Lower left: {}'.format(pr_LL.value))
    time.sleep(1)
```
# Servo Motors Test
## Simple
Just move the arm around
```
import board
import analogio
import pwmio
import time
from adafruit_motor import servo

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

pwm = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
```
This build is using two servo motors to move the flower face in the direction of the Sun.
```
# Libraries we will need.
import board
import analogio
import pwmio
from adafruit_motor import servo
import time

# Create the PWM out objects that the servo motor libraries need.
pwm_horiz = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
pwm_vert = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

# Create the servo motor objects so that it's easy to position.
servo_horiz = servo.Servo(pwm_horiz)
servo_vert = servo.Servo(pwm_vert)

# Sweep the servo motors

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        servo_horiz.angle = angle
        servo_vert.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        servo_horiz.angle = angle
        servo_vert.angle = angle
        time.sleep(0.05)
```