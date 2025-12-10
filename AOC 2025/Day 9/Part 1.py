coords = []
areas = []
with open('input.txt','r') as file:
    for line in file:
        coords.append(line.strip().split(','))
for i in range(len(coords)-1):
    for c in range(1,len(coords)):
        x = int(coords[i][0]) - int(coords[c][0])
        y = int(coords[i][1]) - int(coords[c][1])
        if x < 0:
            x -= 1
            x = x * -1
        else:
            x += 1
        if y < 0:
            y -=1
            y = y * -1
        else:
            y += 1
        area = x * y
        areas.append(area)
print(max(areas))
        
