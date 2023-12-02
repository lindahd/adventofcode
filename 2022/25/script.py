inputs = open("input").read().splitlines()  
 
map_snafu = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}

def snafu_to_decim(snafu):
    total = 0
    for i, digit in enumerate(reversed(snafu)):
        total += map_snafu[digit] * 5 ** (i)
    return total

def decim_to_snafu(n):
    res = ""
    retenue = 0
    while (n > 0) or retenue: 
        rest = n % 5 + retenue 
        if rest == 4:
            res += '-'
            retenue = 1
        elif rest == 3:
            res += '='
            retenue = 1
        elif rest == 5:
            res += '0'
            retenue = 1
        else:
            res += str(rest)
            retenue = 0 
        n = n // 5
    return res[::-1]

sum_snafu = sum([snafu_to_decim(snafu) for snafu in inputs])
print("part 1:", decim_to_snafu(sum_snafu))