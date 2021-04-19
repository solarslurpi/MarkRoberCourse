import board
import analogio

# Hook up the 4 photo resistors
pr_UL = analogio.AnalogIn(board.A2)
pr_UR = analogio.AnalogIn(board.A3)
pr_LR = analogio.AnalogIn(board.A4)
pr_LL = analogio.AnalogIn(board.A5)

# Get an average value
num = 100
UR_list = []
UL_list = []
LL_list = []
LR_list = []

for i in range(num):
    # take a reading
        UR_list.append(pr_UR.value)
        UL_list.append(pr_UL.value)
        LR_list.append(pr_LR.value)
        LL_list.append(pr_LL.value)

print('UL: {}, UR: {}, LR: {}, LL: {}'.format(sum(UL_list)/num,sum(UR_list)/num,sum(LR_list)/num,sum(LL_list)/num))