inputs = open("input").read().splitlines()
import networkx as nx 

# find start S
start_i = [idx for idx, line in enumerate(inputs) if 'S' in line][0]
start_j = [idx for idx, char in enumerate(inputs[start_i]) if char == 'S'][0]
inputs[start_i] = inputs[start_i].replace('S', 'a')

# find target E
target_i = [idx for idx, line in enumerate(inputs) if 'E' in line][0]
target_j = [idx for idx, char in enumerate(inputs[target_i]) if char == 'E'][0]
inputs[target_i] = inputs[target_i].replace('E', 'z')

# build the whole map as a directed graph, because graph is life 
G = nx.DiGraph()
for i, _ in enumerate(inputs):
    for j, char in enumerate(inputs[i]):
        try:
            char_v = inputs[i+1][j]
            G.add_node((i,j), value=char)
            G.add_node((i+1,j), value=char_v)
            if 0 <= abs(ord(char_v) - ord(char)) <= 1:
                G.add_edge((i,j), (i+1,j)) 
                G.add_edge((i+1,j), (i,j)) 
            if ord(char) <= ord(char_v):
                G.add_edge((i+1,j), (i,j)) 
        except IndexError as e :
            pass

        try:
            char_h = inputs[i][j+1]
            G.add_node((i,j), value=char)
            G.add_node((i,j+1), value=char_h)
            if 0 <= abs(ord(char_h) - ord(char)) <= 1:
                G.add_edge((i,j), (i,j+1)) 
                G.add_edge((i,j+1), (i,j)) 
            if ord(char) <= ord(char_h):
                G.add_edge((i,j+1), (i,j)) 
        except IndexError as e :
            pass

print("part 1:", nx.shortest_path_length(G, (start_i, start_j), (target_i, target_j)))

len_simple_path = []
for i in [idx for idx, line in enumerate(inputs) if 'a' in line]:
    list_j = [idx for idx, char in enumerate(inputs[i]) if char == 'a']
    for j in list_j:
        try:
            len_simple_path.append(nx.shortest_path_length(G, (i,j), (target_i, target_j)))
        except:
            # if there is no path
            pass 
print('part 2:', min(len_simple_path))
