inputs = open("input").read().splitlines() 
rocks = [[(int(coords.split(',')[0]), int(coords.split(',')[1])) 
          for coords in line.split(' -> ')] for line in inputs]
START = (500, 0) 

def generate_line_coordinates(min_x, min_y, max_x, max_y):
    x_inter = list(range(min_x+1, max_x)) if min_x != max_x else [max_x]*(max_y-min_y-1)
    y_inter = list(range(min_y+1, max_y)) if min_y != max_y else [max_y]*(max_x-min_x-1)
    return list(zip(x_inter , y_inter))

def build_cave(rocks):
    cave = set()
    limit_min_x = 500
    limit_max_x = 500
    limit_max_y = 0
    for coords in rocks:
        for i in range(len(coords) - 1):
            c_1, c_2 = coords[i], coords[i+1]
            min_x, max_x = sorted([c_1[0], c_2[0]])
            min_y, max_y = sorted([c_1[1], c_2[1]])
            # get x,y limits btw
            limit_min_x = min(limit_min_x, min_x) 
            limit_max_x = max(limit_max_x, max_x) 
            limit_max_y = max(limit_max_y, max_y)
            c_inter = generate_line_coordinates(min_x, min_y, max_x, max_y)
            cave.update(c_inter)
            cave.update([c_1, c_2])
    return cave, limit_min_x, limit_max_x, limit_max_y

def produce_sand(cave, limit_min_x, limit_max_x, limit_max_y):
    has_next = True
    sand = START
    while has_next: 
        # above limits 
        if not limit_min_x < sand[0] < limit_max_x or sand[1] >= limit_max_y:
            return None
        # rest to start point
        if START in cave: 
            return None
        # fall down
        rsand = (sand[0], sand[1] + 1)
        if rsand not in cave:
            sand = rsand
        else: 
            lsand = (rsand[0] - 1, rsand[1])
            rsand = (rsand[0] + 1, rsand[1])
            # try left 
            if lsand not in cave:
                sand = lsand
            # try right 
            elif rsand not in cave:
                sand = rsand
            # rest
            else:
                cave.add(sand)
                return sand
            
cave, limit_min_x, limit_max_x, limit_max_y = build_cave(rocks)
sand = START
count = 0
while sand is not None:
    sand = produce_sand(cave, limit_min_x, limit_max_x, limit_max_y) 
    count += 1
print("part 1:", count - 1)

# part 2, update cave
cave, limit_min_x, limit_max_x, limit_max_y = build_cave(rocks)
c_floor = generate_line_coordinates(limit_min_x-200, 
                                    limit_max_y+2,
                                    limit_max_x+200,                             
                                    limit_max_y+2)
cave.update(c_floor)
sand = START
count = 0
while sand is not None:
    sand = produce_sand(cave, limit_min_x-200, limit_max_x+200, limit_max_y+2) 
    count += 1
print("part 2:", count - 1)