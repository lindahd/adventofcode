inputs = open("input").read().splitlines()
import networkx as nx

G = nx.DiGraph()
# add root
current_dir = '/'
G.add_node(current_dir, type='folder', weight=0)

for i,line in enumerate(inputs[1:]):
    # parse cmd 
    linesplit = line.split(' ')
    if linesplit[:2] == ['$', 'cd']:
        if linesplit[2] == '..':
            # go back
            pred = list(G.predecessors(current_dir))
            if len(pred) != 0:
                # before leaving, count size
                G.nodes[pred[0]]["weight"] += G.nodes[current_dir]["weight"]
                current_dir = pred[0] # previous_dir
        else:
            # step into folder
            current_dir += f"/{linesplit[2]}"
    elif linesplit[:2] == ['$', 'ls']:
        #do nada
        continue
    elif linesplit[0] == 'dir':
        # create folder
        new_dir = f'{current_dir}/{linesplit[1]}'
        G.add_node(new_dir, type='folder', weight=0)
        G.add_edge(current_dir, new_dir)
    else:
        # create file in current folder
        new_file = f'{current_dir}/{linesplit[1]}'
        G.add_node(new_file, type='file', weight=int(linesplit[0]))
        G.add_edge(current_dir, new_file)
        G.nodes[current_dir]["weight"] += int(linesplit[0])        

w_folder = [att['weight'] for node, att in G.nodes().data() if att["type"] == "folder"]
print("part 1:", sum(filter(lambda x: x <= 100000, w_folder)))

#update root size
G.nodes['/']['weight'] = sum([G.nodes[i]['weight']  for i in list(nx.neighbors(G,'/') )])
remaining = 70000000 - G.nodes['/']['weight']
print("part 2:", min(filter(lambda x: x > 30000000-remaining, w_folder)))
