codes,wpaths = {},{}
visited = []
with open('input.txt','r') as file:
    for line in file:
        code = line[:3]
        code1 = line[4:].strip().split(' ')
        codes[code] = []
        for i in code1:
            codes[code].append(i)

            
def win(thing):
    if thing in wpaths:
        return wpaths[thing]
    if thing == 'out':
        return 1
    total = 0
    for p in codes[thing]:
        total += win(p)
    wpaths[thing] = total
    return total


ans = win('you')
print(ans)
