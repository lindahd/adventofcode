
import math
inputs = open("input").read().split('\n\n')
# list of the seven maps each with list of (destination range start, source range start, range length)
maps = []
for part in inputs:
    if '\n' in part:
        lines = part.split('\n')
        maps.append([tuple(map(int,x.split())) for x in lines[1:]])
    else:
        seeds = list(map(int, part.split(':')[-1].split()))

def get_next(value, current_map):
    for dest, source, range in current_map:
        if source <= value < source + range:
            return dest + (value - source)
    return value

def get_final_location(seed, maps):
    next_value = seed
    for current_map in maps:
        next_value = get_next(next_value, current_map)
    return next_value

res = min([get_final_location(seed, maps) for seed in seeds])

print(f"result part 1: {res}")

#who's the brut? me? :o
res = math.inf
for seed_min, l in list(zip(seeds, seeds[1:]))[::2]:
    for seed in range(seed_min, seed_min + l):
        loc = get_final_location(seed, maps)
        if loc < res: res = loc

print(f"result part 2: {res}")
