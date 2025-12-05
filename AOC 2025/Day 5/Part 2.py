ranges = []
nums = []
trueranges = []
total = 0
mergedranges = []
with open('input.txt','r') as file:
    for line in file:
        ranges.append(line.strip())

for i in ranges:
    curr = i.split('-')
    trueranges.append([int(curr[0]), int(curr[1])])
trueranges.sort()

currentstart = int(trueranges[0][0])
currentend = int(trueranges[0][1])

for i in range(1, len(trueranges)):
    nextstart = int(trueranges[i][0])
    nextend = int(trueranges[i][1])
    if nextstart <= currentend + 1:
        if nextend > currentend:
            currentend = nextend
    else:
        mergedranges.append([currentstart, currentend])
        currentstart = nextstart
        currentend = nextend
mergedranges.append([currentstart, currentend])

for i in range(len(mergedranges)):
    total += mergedranges[i][1] - mergedranges[i][0] + 1
print(total)
