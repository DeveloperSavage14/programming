lines= []
total = 0
with open('input.txt','r') as file:
    for line in file:
        lines.append(list(line))


for i in range(len(lines)):
    if i == 0:
        continue
    for c in range(len(lines[i])):
        if lines[i][c] == '^' and lines[i-1][c] == '|':
            total += 1
            if c > 0:
                lines[i][c-1] = '|'
            if c < len(lines[i]):
                lines[i][c+1] = '|'
        elif lines[i][c] == '.' and lines[i-1][c] == '|':
            lines[i][c] = '|'
        elif lines[i][c] == '.' and lines[i-1][c] == 'S':
            lines[i][c] = '|'
print(total)
print(lines)
                
