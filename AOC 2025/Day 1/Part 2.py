lines = []
start = 50
total = 0
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())
    for i in range(len(lines)):
        if lines[i][0] == 'R':
            for _ in range(int(lines[i][1:])):
                start = start + 1
                if start == 100:
                    total += 1
                    start = 0
        elif lines[i][0] == 'L':
            for c in range(int(lines[i][1:])):
                start = start - 1
                if c == 0:
                    if start == -1:
                        start = 99
                    if start == 0:
                        total += 1
                else:
                    if start == 0:
                        total += 1
                    if start == -1:
                        start = 99
print(total)
