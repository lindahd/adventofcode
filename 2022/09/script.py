inputs = open("input").read().splitlines()
import numpy as np

direction = {'U': [1, 0], 'D': [-1, 0], 'R': [0, 1], 'L': [0, -1]}   
moves = [[direction[m.split(' ')[0]]] * int(m.split(' ')[1]) for m in inputs] 
moves = [m for move in moves for m in move]

def update_position(head_pos, tail_pos):
    distance = head_pos - tail_pos
    move_tail = [0, 0]
    if list(abs(distance)) in [[2, 1], [1, 2]]:
        move_tail[np.argmax(abs(distance))] = np.sign(distance[np.argmax(abs(distance))])
        move_tail[np.argmin(abs(distance))] = np.sign(distance[np.argmin(abs(distance))])
    elif list(abs(distance)) in [[2, 0], [0, 2]]:
        move_tail[np.argmax(abs(distance))] = np.sign(distance[np.argmax(abs(distance))])
    elif list(abs(distance)) in [[2, 2], [2, 2]]:
        move_tail = [np.sign(distance[0]), np.sign(distance[1])]
    return move_tail + tail_pos

snake = {i:[np.array([0, 0])] for i in range(10)}
for i, m in enumerate(moves):
    # update head position
    snake[0].append(snake[0][-1] + m)
    # update successively the followers
    for s in range(1, 10):
        snake[s].append(update_position(snake[s-1][-1], snake[s][-1]))

print("part 1:", len(np.unique(snake[1], axis=0)))
print("part 2:", len(np.unique(snake[9], axis=0)))