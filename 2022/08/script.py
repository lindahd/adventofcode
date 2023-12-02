import numpy as np

inputs = open("input").read().splitlines()
map = np.array([list(i) for i in inputs] , dtype=int)

count = map.shape[0]*2 + map.shape[1]*2 - 4
for i in range(1, map.shape[0]-1):
    for j in range(1, map.shape[1]-1): 
        cond_up = all(map[i,j] > x for x in map[:i,j])
        cond_down = all(map[i,j] > x for x in map[i+1:,j]) 
        cond_left = all(map[i,j] > x for x in map[i,:j])  
        cond_right = all(map[i,j] > x for x in map[i,j+1:]) 
        count += 1 if cond_left or cond_right or cond_down or cond_up else 0
print("part 1:", count)

def count_visible_trees(val, trees, text=""):
    s = 0 
    for x in trees: 
        s += 1 
        if not val > x: 
            break
    return s

scenic = np.zeros_like(map)
for i in range(1, map.shape[0]-1):
    for j in range(1, map.shape[1]-1):
        count_up = count_visible_trees(map[i,j], reversed(map[:i,j]) )
        count_down = count_visible_trees(map[i,j], map[i+1:,j])
        count_left = count_visible_trees(map[i,j], reversed(map[i,:j]))
        count_right = count_visible_trees(map[i,j], map[i,j+1:])
        scenic[i,j] = count_up*count_down*count_left*count_right 
print("part 2:", np.max(scenic))
