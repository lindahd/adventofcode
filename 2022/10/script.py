inputs = open("input").read().splitlines()
cmds = [line.split(" ")[0] for line in inputs]
values = []
for i, cmd in enumerate(cmds):
    if cmd == 'noop':
        values.append(0)
    else:
        val = int(inputs[i].split(' ')[1])
        values.append(0); values.append(val)    
        
def signal_strength(values, cycle):
    return (1 + sum(values[:cycle-1])) * cycle

print("part 1:", sum([signal_strength(values, i) for i in range(20,221,40)]))

import numpy as np
import matplotlib.pyplot as plt
screen = np.zeros([6, 40])

for row in range(6):
    for crt in range(40):
        crt_current = crt + 40*row
        val = sum(values[:crt_current]) + 1
        screen[row, crt] = 1 if crt == val-1 or crt == val or crt == val+1 else 0
plt.spy(screen)
print("part 2: EGLHBLFJ")