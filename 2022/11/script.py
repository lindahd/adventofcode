from functools import reduce
inputs = open("input").read().splitlines()

def extract_monkey(inputs):
    nb_monkey = int(len(inputs)/7) + 1
    monkey = {}
    for i in range(nb_monkey):
        data = inputs[7*i:7*(i+1)]
        monkey_data = {
            'items': [int(item.replace(',', '')) for item in data[1].split(' ')[4:]],
            'oper': eval(f"lambda old: {data[2].split('= ')[1]}"),
            'test': int(data[3].split('by ')[1]),
            'result': {True: int(data[4].split('monkey ')[1]),
                       False: int(data[5].split('monkey ')[1])},
            'count':0
            }
        monkey[i] = monkey_data
    return monkey

# 20 rounds
monkey = extract_monkey(inputs)
pgcm = reduce((lambda x, y: x * y), 
              ([m["test"] for m in monkey.values()]))

def compute_rounds(rounds, monkey, part):
    for _ in range(rounds):
        for i in range(len(monkey)):
            items_to_inspect = monkey[i]['items'].copy()
            for item in items_to_inspect:
                monkey[i]['count'] += 1
                worry_level = monkey[i]['oper'](item) % pgcm
                if part == 1:
                    worry_level //= 3
                test = monkey[i]['test']
                next_monkey = monkey[i]['result'][worry_level % test == 0]
                monkey[next_monkey]['items'].append(worry_level)
                # print(f"send from {i} to {next_monkey }")
                monkey[i]['items'].remove(item)

compute_rounds(20, monkey, 1)
print("part 1:", reduce((lambda x, y: x * y), 
                        sorted([m["count"] for m in monkey.values()])[-2:]))


# 10000 rounds
monkey = extract_monkey(inputs)
compute_rounds(10000, monkey, 2)
print("part 2:", reduce((lambda x, y: x * y), 
                         sorted([m["count"] for m in monkey.values()])[-2:]))