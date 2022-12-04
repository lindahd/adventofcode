inputs = open("input").read().splitlines()

letters = [chr(i) for i in range(97, 123)] + [chr(i).upper() for i in range(97, 123)]
priority = dict(zip(letters, range(1,53)))

sum_prio = 0
for rucksack in inputs:
    r1 = rucksack[:len(rucksack)//2]
    r2 = rucksack[len(rucksack)//2:]
    common = list(set(r1).intersection(set(r2)))
    sum_prio += priority[common[0]]
print("part 1:", sum_prio)

sum_prio = 0
for i in range(0, len(inputs), 3):
    common = list(set(inputs[i]).intersection(set(inputs[i+1])).intersection(set(inputs[i+2])))
    sum_prio += priority[common[0]]
print("part 2:", sum_prio)