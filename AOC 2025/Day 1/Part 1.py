lines = []
start = 50
total = 0
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())
    for i in range(len(lines)):
        if lines[i][0] == 'R':
            start = start + int(lines[i][1:])
            while start >= 100:
                start -= 100
        elif lines[i][0] == 'L':
            start = start - int(lines[i][1:])
            while start < 0:
                start = 100 + start
        if start == 0:
            total += 1
print(total)
