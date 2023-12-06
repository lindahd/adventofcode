import numpy as np
import re

inputs = open("input").read().splitlines()
lines = [x.split(':')[-1].split(';') for x in inputs]

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14
colors = ['red', 'green', 'blue']


def get_cubes(cubes_set):
    cubes_set = cubes_set.split(',')
    cubes = {c: 0 for c in colors}
    cvalues = [int(re.sub(r"[a-zA-Z ]", '', t)) for t in cubes_set]
    ccolors = [re.sub(r"[\d+ ]", '', t) for t in cubes_set]
    for c in colors:
        if c in ccolors:
            cubes[c] = cvalues[ccolors.index(c)]
    return cubes


# build list of dict
games = [[get_cubes(cubes_set) for cubes_set in game] for game in lines]

# part 1
possible_game_list = []
for i, game in enumerate(games):
    possible = all(list(map(lambda cubes_set: cubes_set['red'] <= RED_MAX and
                                              cubes_set['green'] <= GREEN_MAX and
                                              cubes_set['blue'] <= BLUE_MAX, game)))
    if possible: possible_game_list.append(i + 1)
res = sum(possible_game_list)
print(f"result part 1: {res}")


# part 2
def get_max_color(game):
    green = max([c['green'] for c in game])
    red = max([c['red'] for c in game])
    blue = max([c['blue'] for c in game])
    return green * red * blue


res = sum(get_max_color(game) for game in games)

print(f"result part 2: {res}")
