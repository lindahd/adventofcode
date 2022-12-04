inputs = open("input").read()
list_adv = [i.split(' ')[0]  for i in inputs.split('\n')]
list_me = [i.split(' ')[1] for i in inputs.split('\n')]

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
dict_result = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
                    }
dict_bonus = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
for i in range(len(list_adv)):
    score += dict_result[list_adv[i], list_me[i]] + dict_bonus[list_me[i]]

print("part 1:", score)

dict_result_2 = {
    ('A', 'X'): 0,
    ('A', 'Y'): 3,
    ('A', 'Z'): 6,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 0,
    ('C', 'Y'): 3,
    ('C', 'Z'): 6,
                    }
dict_map_bonus = {
    ('A', 'X'): 'Z',
    ('A', 'Y'): 'X',
    ('A', 'Z'): 'Y',
    ('B', 'X'): 'X',
    ('B', 'Y'): 'Y',
    ('B', 'Z'): 'Z',
    ('C', 'X'): 'Y',
    ('C', 'Y'): 'Z',
    ('C', 'Z'): 'X',
                    }
score = 0
for i in range(len(list_adv)):
    score += dict_result_2[list_adv[i], list_me[i]] + dict_bonus[dict_map_bonus[list_adv[i], list_me[i]]]

print("part 2:", score)