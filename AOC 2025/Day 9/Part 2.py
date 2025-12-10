
points = []
with open('input.txt','r') as file:
    p = 0
    for line in file:
        parts = line.strip().split(',')
        points.append((int(parts[0]), int(parts[1])))
edges = []

for i in range(len(points)):
    if i == len(points)-1:
        l = points[0]
    else:
        l = points[i+1]
    edges.append([points[i][0], points[i][1], l[0], l[1]])

bigarea = 0
for i in range(len(points)):
    for p in range(i+1, len(points)):
        if points[i][0] < points[p][0]:
            minx = points[i][0]
            maxx = points[p][0]
        else:
            minx = points[p][0]
            maxx = points[i][0]
        if points[i][1] < points[p][1]:
            miny = points[i][1]
            maxy = points[p][1]
        else:
            miny = points[p][1]
            maxy = points[i][1]
        w = maxx - minx
        h = maxy - miny
        area = (w+1) * (h+1)
        if area <= bigarea:
            continue
        valid = True
        print("Validating")
        mx = (minx+maxx)/2
        my = (miny+maxy)/2
        c = 0
        for q in edges:
            if q[0] == q[2]:
                wx = q[0]
                if q[1] < q[3]:
                    yl = q[1]
                    yh = q[3]
                else:
                    yl = q[3]
                    yh = q[1]
                if wx > mx:
                    if yl <= my:
                        if my < yh:
                            c += 1
        if c % 2 == 0:
            valid = False
        print("Working")
        if valid:
            for q in edges:
                if q[0] == q[2]:
                    wx = q[0]
                    if q[1] < q[3]:
                        yl = q[1]
                        yh = q[3]
                    else:
                        yl = q[3]
                        yh = q[1]
                    if mx < wx:
                        if wx < maxx:
                            if miny > yl:
                                ol = miny
                            else:
                                ol = yl
                            if maxy < yh:
                                oh = maxy
                            else:
                                oh = yh
                            if ol < oh:
                                valid = False
                                break
                else:
                    wy = q[1]
                    if q[0] < q[2]:
                        xl = q[0]
                        xh = q[2]
                    else:
                        xl = q[2]
                        xh = q[0]

                    if miny < wy:
                        if wy < maxy:
                            if minx > xl:
                                ol = minx
                            else:
                                ol = xl
                            if maxx < xh:
                                oh = maxx
                            else:
                                oh = xh
                            if ol < oh:
                                valid = False
                                break
        print("Almost Done")
        if valid:
            bigarea = area
print(bigarea)
        





        
       

        
