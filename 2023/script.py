import numpy as np
import re
inputs = open("input").read().splitlines()

# part 1
only_d = [re.sub(r"[a-zA-Z]",'', x) for x in inputs]
res = sum([int(''.join([x[0], x[-1]])) for x in only_d])
print(f"result part 1: {res}")

# part 2
numbers = {'one': '1', 'two': '2', 'three': '3',
           'four': '4', 'five': '5', 'six': '6',
           'seven': '7', 'eight': '8', 'nine': '9',
           '1': '1', '2': '2', '3': '3',
           '4': '4', '5': '5', '6': '6',
           '7': '7', '8': '8', '9': '9'
           }
def findall(p, s):
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

only_numbers = []
for x in inputs:
    res_x = {}
    for y in numbers.keys():
        res_x.update({i: numbers[y] for i in list(findall(y, x))})
    only_numbers.append(dict(sorted(res_x.items())))

res = sum([int(''.join([list(x.values())[0],
                        list(x.values())[-1]])) for x in only_numbers])

print(f"result part 2: {res}")