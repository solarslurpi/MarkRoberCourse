import board
import analogio
import pwmio
from adafruit_motor import servo
import simpleio
import time

# Calibration Values
UL_low = 170.56
UL_high = 62144.3
UR_low = 180.8
UR_high = 61040.0
LR_low = 235.2
LR_high = 48747.8
LL_low = 174.08
LL_high = 60482.2

# Hook up the 4 photo resistors
pr_UL = analogio.AnalogIn(board.A2)
pr_UR = analogio.AnalogIn(board.A3)
pr_LR = analogio.AnalogIn(board.A4)
pr_LL = analogio.AnalogIn(board.A5)

# Create the PWM out objects that the servo motor libraries need.
pwm_horiz = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)
pwm_vert = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)

# Create the servo motor objects so that it's easy to position.
servo_horiz = servo.Servo(pwm_horiz)
servo_vert = servo.Servo(pwm_vert)
servo_horiz.angle = 180
servo_vert.angle = 180

# Just keep solar surfing...
while True:
    time.sleep(2)  # Let's wait a bit in between readings...
    # Get Readings and normalize to high low
    ul_value  = simpleio.map_range(pr_UL.value,UL_low,UL_high,0,100)
    ur_value  = simpleio.map_range(pr_UR.value,UR_low,UR_high,0,100)
    lr_value  = simpleio.map_range(pr_LR.value,LR_low,LR_high,0,100)
    ll_value  = simpleio.map_range(pr_LL.value,LL_low,LL_high,0,100)
    print('ul: {}, ur: {}, lr: {}, ll: {}'.format(ul_value,ur_value,lr_value,ll_value))
    # Sleep here because continue goes to the top of the while loop.

    print('*** SERVO_HORIZ ANGLE: {}'.format(servo_horiz.angle))
    # move the flower base
    
    # Horizontal (left - right)
    if (ul_value > ur_value ):
        print('UL > UR')
        try:
            servo_horiz.angle -= 2
            print('-- horiz in try-- {}'.format(servo_horiz.angle))
        except:
            # servo_horiz.angle = 180
            print(servo_horiz.angle)
            pass
    else:
        print('UR > UL')
        try:
            servo_horiz.angle += 2
            print('-- horiz in try-- {}'.format(servo_horiz.angle))
        except:
            # servo_horiz.angle = 0
            print(servo_horiz.angle)
            pass
    if (ll_value > lr_value ):
        print('LL > LR')
        try:
            servo_horiz.angle -= 2
            print('-- horiz in try-- {}'.format(servo_horiz.angle))
        except:
            # servo_horiz.angle = 180
            print(servo_horiz.angle)
            pass
    else:
        print('LR > LL')
        try:
            servo_horiz.angle += 2
            print('-- horiz in try-- {}'.format(servo_horiz.angle))
        except:
            # servo_horiz.angle = 0
            print(servo_horiz.angle)
            pass
            
    # Up - Down servo
    print('*** SERVO_VERT ANGLE: {}'.format(servo_vert.angle))  
    if (ul_value > ur_value ):
        print('UL > UR')
        try:
            servo_vert.angle -= 2
            print('-- vert in try-- {}'.format(servo_vert.angle))
        except:
            # servo_horiz.angle = 180
            print(servo_vert.angle)
            pass
    else:
        print('UR > UL')
        try:
            servo_vert.angle += 2
            print('-- vert in try-- {}'.format(servo_vert.angle))
        except:
            # servo_horiz.angle = 0
            print(servo_vert.angle)
            pass
    if (ll_value > lr_value ):
        print('LL > LR')
        try:
            servo_vert.angle -= 2
            print('-- vert in try-- {}'.format(servo_vert.angle))
        except:
            # servo_horiz.angle = 180
            print(servo_vert.angle)
            pass
    else:
        print('LR > LL')
        try:
            servo_vert.angle += 2
            print('-- vert in try-- {}'.format(servo_vert.angle))
        except:
            # servo_horiz.angle = 0
            print(servo_vert.angle)
            pass
