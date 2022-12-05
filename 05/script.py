inputs = open("input").read().splitlines()
stacks = open("stacks").read().splitlines()

def load_stack():
    # Prepare stacks
    nb_of_stack = int(stacks[-1].split('  ')[-1])
    dict_stack = {i+1:[] for i in range(nb_of_stack)} 
    index_crate = []
    for line in stacks[:-1]:
        crate_line = [line[1+i] for i in range(0, nb_of_stack*4, 4)]
        for i in range(nb_of_stack):
            if len(crate_line[i].strip()) != 0: dict_stack[i + 1].append(crate_line[i])

    # Reverse order of stacks
    [v.reverse() for k, v in dict_stack.items()]
    return dict_stack

dict_stack = load_stack()
for move in inputs:
    val = int(move.split(' ')[1])
    depart = int(move.split(' ')[3])
    arrivee = int(move.split(' ')[5])
    for i in range(val):
        dict_stack[arrivee].append(dict_stack[depart].pop())
top_crate = [s[-1] for s in dict_stack.values()]
print('part 1:', ''.join(top_crate))

dict_stack = load_stack()
for move in inputs:
    val = int(move.split(' ')[1])
    depart = int(move.split(' ')[3])
    arrivee = int(move.split(' ')[5])
    dict_stack[arrivee].extend(dict_stack[depart][-val:])
    del dict_stack[depart][-val:]
top_crate = [s[-1] for s in dict_stack.values()]
print('part 2:', ''.join(top_crate))
