inputs = open("input").read()

def find_marker(length):
    for char in range(length, len(inputs)):
        if len(set(inputs[char-length:char])) == length:
            return char
print("part 1:", find_marker(4) )
print("part 2:", find_marker(14) )