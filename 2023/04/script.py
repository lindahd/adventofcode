inputs = open("input").read().splitlines()

winning = [set(x.split(':')[-1].split('|')[0].strip().split()) for x in inputs]
tirage = [set(x.split(':')[-1].split('|')[1].strip().split()) for x in inputs]
matches = [w.intersection(t) for w,t in zip(winning, tirage)]
points = [2**(len(x)-1) if len(x) > 0 else 0 for x in matches]

print(f"result part 1: {sum(points)}")

cards = [1] * len(inputs)
for c in range(len(inputs)):
    for i in range(c + 1, c + len(matches[c]) + 1):
        cards[i] += cards[c]

print(f"result part 2: {sum(cards)}")
