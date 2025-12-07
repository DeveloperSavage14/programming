lines= []
counter = []
total = 0
with open('input.txt','r') as file:
    for line in file:
        lines.append(list(line.strip()))
for i in range(len(lines)):
    curr = []
    for c in range(len(lines[i])):
        curr.append(0)
    counter.append(curr)

for i in range(len(lines)):
    for c in range(len(lines[i])):
        if lines[i][c] == 'S':
            counter[i][c] = 1

for i in range(1,len(lines)):
    for c in range(len(lines[i])):
        time = counter[i-1][c]
        if time > 0:
            if lines[i][c] == '^':
                if c > 0:
                    counter[i][c-1] += time
                if c < len(lines[i]) - 1:
                    counter[i][c+1] += time
            else:
                counter[i][c] += time
for i in range(len(counter[-1])):
    total += int(counter[-1][i])
print(total)
                
