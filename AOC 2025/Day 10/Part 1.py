from itertools import combinations
buttons = []
lights = []
gtotal = 0
with open('input.txt', 'r') as file:
    for line in file:
        curr = line.strip().split(" ")
        lights.append(curr[0][1:-1])
        curr.pop(0)
        curr.pop(-1)
        buttons.append(curr)

for i in range(len(lights)):
    butvals = []
    binary = ""
    length = len(lights[i])
    for c in range(length):
        if lights[i][c] == "#":
            binary += '1'
        else:
            binary += '0'
    trueval = int(binary, 2)
    numbut = len(buttons[i])
    for c in range(numbut):
        clean = buttons[i][c].strip("()").split(',')
        total = 0
        for p in clean:
            power = length - 1 - int(p)
            val = 2**power
            total = total + val
        butvals.append(total)
    found = False
    for s in range(numbut + 1):
        if found:
            break
        for combo in combinations(butvals, s):
            current = 0
            for v in combo:
                current = current ^ v
            if current == trueval:
                gtotal += s
                found = True
                break
print(gtotal)
