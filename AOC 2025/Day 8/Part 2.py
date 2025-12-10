import time as t
start = t.time()
coords = []
pairs = []
links = []
curr = []
final = []
with open('input.txt','r') as file:
    for line in file:
        coords.append(line.strip().split(','))
        links.append([line.strip().split(',')])

for i in range(len(coords)):
    for c in range(i+1, len(coords)):
        distance = (int(coords[i][0])-int(coords[c][0]))**2 + (int(coords[i][1])-int(coords[c][1]))**2 + (int(coords[i][2])-int(coords[c][2]))**2
        pairs.append([distance,coords[i],coords[c]])

pairs.sort()

print('Pairs Sorted')
for i in range(1,len(pairs)):
    pos1 = -1
    pos = -1
    for c in range(len(links)):
        if pairs[i][1] in links[c]:
            pos1 = c
        if pairs[i][2] in links[c]:
            pos = c
    if pos1 != -1 and pos != -1 and pos1 != pos:
        links[pos1].extend(links[pos])
        links.pop(pos)
        if len(links) == 1 and i > 2:
            u = pairs[i][-1]
            y = pairs[i][-2]
            ans = int(u[0]) * int(y[0])
            print(ans)
            end = t.time() - start
            break
print('Nodes Connected')
print(f'Your code took {end} seconds to run')
