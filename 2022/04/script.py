inputs = open("input").read().splitlines()

assign_1 = [range(int(i.split(',')[0].split('-')[0]), 1+int(i.split(',')[0].split('-')[1])) for i in inputs]
assign_2 = [range(int(i.split(',')[1].split('-')[0]), 1+int(i.split(',')[1].split('-')[1])) for i in inputs]

print("part 1:",sum([len(set(a1).intersection(set(a2))) == min(len(a1), len(a2)) for a1, a2 in zip(assign_1, assign_2)]))
print("part 2:",sum([len(set(a1).intersection(set(a2))) > 0 for a1, a2 in zip(assign_1, assign_2)]))
