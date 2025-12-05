ranges = []
stock = []
trueranges = []
total = 0
with open('input.txt','r') as file:
    for line in file:
        ranges.append(line.strip())
with open('input2.txt','r') as file:
    for line in file:
        stock.append(line.strip())
for i in ranges:
    curr = i.split('-')
    trueranges.append(curr)

for i in stock:
    skip = False
    for p in range(len(trueranges)):
        if skip:
            continue
        if int(i) <= int(trueranges[p][1]) and int(i) >= int(trueranges[p][0]):
            total += 1
            skip = True
print(total)

            
