with open("input1") as fp:
    current_calo = 0
    list_calo = []
    for line in fp.readlines():
        if len(line.strip()) != 0: 
            current_calo += int(line.strip()) 
        else:
            list_calo.append(current_calo)
            current_calo = 0
print("part 1:", max(list_calo)) 
print("part 2:", sum(sorted(list_calo)[-3:]))     