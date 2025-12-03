lines = []
total = 0
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())
    for i in lines:
        p = 0
        for q in range(len(i) - 11):
            for w in range(q + 1, len(i)-10):
                for e in range(w+1, len(i) - 9):
                    for r in range(e + 1, len(i)-8):
                        for t in range(r+1, len(i) - 7):
                            for y in range(t + 1, len(i)-6):
                                for u in range(y+1, len(i) - 5):
                                    for a in range(u + 1, len(i)-4):
                                        for s in range(a+1, len(i) - 3):
                                            for d in range(s + 1, len(i)-2):
                                                for f in range(d+1, len(i) - 1):
                                                    for g in range(f + 1, len(i)):
                                                        num = str(i[q]) + str(i[w])+str(i[e]) + str(i[r])+str(i[t]) + str(i[y])+str(i[u]) + str(i[a])+str(i[s]) + str(i[d])+str(i[f]+str(i[g]))
                                                        v = int(num)
                                                        if v > p:
                                                            p = v
        
        total = total + p
print(total)
