coords = []
pairs = []
links = []
curr = []
final = []
with open('input.txt','r') as file:
    for line in file:
        coords.append(line.strip().split(','))

for i in range(len(coords)):
    for c in range(i+1, len(coords)):
        distance = (int(coords[i][0])-int(coords[c][0]))**2 + (int(coords[i][1])-int(coords[c][1]))**2 + (int(coords[i][2])-int(coords[c][2]))**2
        pairs.append([distance,coords[i],coords[c]])

pairs.sort()
curr.append(pairs[0][1])
curr.append(pairs[0][2])
links.append(curr)
curr = []
print('Pairs Sorted')
for i in range(1,1000):
    pos1 = -1
    pos = -1
    curr = []
    for c in range(len(links)):
        if pairs[i][1] in links[c]:
            pos1 = c
        elif pairs[i][2] in links[c]:
            pos = c
    if pos1 == -1 and pos == -1:
        links.append([pairs[i][1],pairs[i][2]])
    elif pos1 != -1 and pos == -1:
        if pairs[i][2] not in links[pos1]:
            links[pos1].append(pairs[i][2])
    elif pos1 == -1 and pos != -1:
        if pairs[i][1] not in links[pos]:
            links[pos].append(pairs[i][1])
    elif pos1 != -1 and pos != -1:
        if pos1 == pos:
            continue
        else:
            t = links[pos1]
            s = links[pos]

            for p in s:
                if p not in t:
                    t.append(p)
            links.pop(pos)
print('Nodes Connected')
for i in links:
    final.append(len(i))
final.sort()
total = final[-1] * final[-2] * final[-3]
print(total)
