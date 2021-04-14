import board
import analogio
import time
pr_UR = analogio.AnalogIn(board.A3)
pr_UL = analogio.AnalogIn(board.A2)
pr_LR = analogio.AnalogIn(board.A4)
pr_LL = analogio.AnalogIn(board.A5)

while True:
    print('Upper right: {}'.format(pr_UR.value))
    print('Upper left: {}'.format(pr_UL.value))
    print('Lower right: {}'.format(pr_LR.value))
    print('Lower left: {}'.format(pr_LL.value))
    time.sleep(1)