import numpy as np
inputs = open("input").read().splitlines()

time, distance = [list(map(int,x.split(':')[-1].split())) for x in inputs]

res_by_race = [sum((t_i * (max(0, t - t_i)) > d) for t_i in range(1, t + 1)) for t,d in zip(time, distance)]

print(f"result part 1: {np.prod(res_by_race)}")

t = int(''.join(str(x) for x in time))
d = int(''.join(str(x) for x in distance))

res_by_race = sum((t_i * (max(0, t - t_i)) > d) for t_i in range(1, t + 1))

print(f"result part 2: {res_by_race}")