monkeys = {line.split(': ')[0]:line.split(': ')[1] for line in open("21/test").read().splitlines()}

# def eval_operation(monkeys, key):
#     val = monkeys[key]
#     if ' ' in val:
#         val = val.split(' ')
#         cmd = f"eval_operation(monkeys, '{val[0]}') {val[1]} eval_operation(monkeys, '{val[2]}')"
#     else:
#         cmd = f"int({val})" 
#     return eval(cmd) 
# print("part 1:", eval_operation(monkeys, 'root'))

def get_operation(monkeys, key):
    cmd = monkeys[key]
    if ' ' in cmd:
        val = cmd.split(' ')
        cmd = f"({get_operation(monkeys, val[0])} {val[1]} {get_operation(monkeys, val[2])})"
    return cmd 
print("part 1:", eval(get_operation(monkeys, 'root')))

# Part 2 
from sympy import sympify, solve
monkeys['root'] = monkeys['root'].replace('+', '-')
monkeys['humn'] = "x"
equation = get_operation(monkeys, 'root')
print("part 2:", solve(sympify(equation))[0])
