inputs = list(filter(lambda x: len(x)!=0, open("input").read().splitlines()))
inputs = [eval(i) for i in inputs]
from itertools import zip_longest

def compare(left, right):
    """ returns True if right order """
    result = None
    for litem, ritem in zip_longest(left, right):
        if result is None:
            if isinstance(litem, list) and isinstance(ritem, list):
                result = compare(litem, ritem)
            elif isinstance(litem, int) and isinstance(ritem, list):
                result = compare([litem], ritem) 
            elif isinstance(litem, list) and isinstance(ritem, int):
                result = compare(litem, [ritem])
            else:
                if ritem == litem:
                    continue
                elif ritem is None:
                    result = result if result is not None else False 
                elif litem is None:
                    result = True 
                elif litem < ritem:
                    return True
                elif ritem < litem:
                    return False
    return result

result = []
for i, (left, right) in enumerate(zip(inputs[::2], inputs[1::2])):
    res = compare(left, right)
    if res: 
        result.append(i + 1)  
print("part 1:", sum(result))  # 1 2 4 6 true

inputs.append([[2]])
inputs.append([[6]])

from functools import cmp_to_key

inputs_sorted = sorted(inputs, key=cmp_to_key(lambda a, b : 1 if compare(a, b) else -1 if compare(b, a) else 0),
                      reverse=True)

print("part 2:", (1+inputs_sorted.index([[6]]))*(1+inputs_sorted.index([[2]])))