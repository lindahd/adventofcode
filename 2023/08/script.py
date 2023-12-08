import networkx as nx
import re

inputs = open("input").read().splitlines()
instruction = inputs[0]
inputs = list(map(lambda x: re.sub(r'\(|\)|,', '', x).split(), inputs[2:]))
nodes_list = {x[0]: (x[2], x[3]) for x in inputs}

# build the network
G = nx.DiGraph()
for name, (l, r) in nodes_list.items():
    G.add_node(name, L=l, R=r)
    G.add_edge(name, r)
    G.add_edge(name, l)

# apply instruction
next_elem = 'AAA'
times = 0
while next_elem != 'ZZZ':
    for i in instruction:
        next_elem = G.nodes[next_elem][i]
    times += 1
res = times * len(instruction)

print(f"result part 1: {res}")


def ppcm(*n):
    def _pgcd(a, b):
        while b: a, b = b, a % b
        return a

    p = abs(n[0] * n[1]) // _pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p * x) // _pgcd(p, x)
    return p


def get_final_step_to_reach_Z(node):
    next_elem = node
    times = 0
    while next_elem[-1] != 'Z':
        for i in instruction:
            next_elem = G.nodes[next_elem][i]
        times += 1
    return times * len(instruction)


nodes_end_A = list(filter(lambda x: x[-1] == 'A', nodes_list.keys()))
res = [get_final_step_to_reach_Z(node) for node in nodes_end_A]

print(f"result part 2: {ppcm(*res)}")
