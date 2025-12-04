lines = []
total = 0
change = True
with open('input.txt','r') as file:
    for line in file:
        lines.append(line.strip())
    while change == True:
        change = False
        for i in range(len(lines)):
            for p in range(len(lines[i])):
                surround = 0
                if lines[i][p] == '.' or lines[i][p] == 'x':
                    continue
                if i != 0 and i != len(lines)-1 and p != 0 and p != len(lines[i]) - 1:
                    for l in range(-1,2):
                        for c in range(-1,2):
                            if c == 0 and l == 0:
                                continue
                            if lines[i+l][p+c] == '@':
                                surround += 1
                    if surround < 4:
                        total += 1
                        line = list(lines[i])
                        line[p] = 'x'
                        lines[i] = line
                        change = True
                else:
                    if i == 0 and p != 0 and p != len(lines[i])-1:
                        for l in range(2):
                            for c in range(-1,2):
                                if c == 0 and l == 0:
                                    continue
                                if lines[i+l][p+c] == '@':
                                    surround += 1
                        if surround < 4:
                            total += 1
                            line = list(lines[i])
                            line[p] = 'x'
                            lines[i] = line
                            change = True
                    elif i == len(lines) - 1 and p != 0 and p != len(lines[i])-1:
                        for l in range(-1,1):
                            for c in range(-1,2):
                                if c == 0 and l == 0:
                                    continue
                                if lines[i+l][p+c] == '@':
                                    surround += 1
                        if surround < 4:
                            line = list(lines[i])
                            line[p] = 'x'
                            lines[i] = line
                            total += 1
                            change = True
                    elif p == 0 and i != 0 and i != len(lines)-1:
                        for l in range(-1,2):
                            for c in range(2):
                                if c == 0 and l == 0:
                                    continue
                                if lines[i+l][p+c] == '@':
                                    surround += 1
                        if surround < 4:
                            line = list(lines[i])
                            line[p] = 'x'
                            lines[i] = line
                            total += 1
                            change = True
                    elif p == len(lines[i])-1 and i != 0 and i != len(lines)-1:
                        for l in range(-1,2):
                            for c in range(-1,1):
                                if c == 0 and l == 0:
                                    continue
                                if lines[i+l][p+c] == '@':
                                    surround += 1
                        if surround < 4:
                            line = list(lines[i])
                            line[p] = 'x'
                            lines[i] = line
                            total += 1
                            change = True
                    elif (p == 0 or p == len(lines[i])-1)and(i == 0 or i == len(lines)-1):
                        total += 1
                        line = list(lines[i])
                        line[p] = 'x'
                        lines[i] = line
                        change = True
print(total)
