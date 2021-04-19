# Libraries we will need.
import board
import analogio
import pwmio
from adafruit_motor import servo
import time

# Create the PWM out objects that the servo motor libraries need.
pwm_horiz = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
pwm_vert = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)

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