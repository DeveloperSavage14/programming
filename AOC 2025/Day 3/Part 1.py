lines = []
total = 0
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())
    for i in lines:
        p = 0
        for c in range(0,len(i)-1):
            for b in range(1,len(i)):
                num = str(i[c])+str(i[b])

                v = int(num)
                if v > p:
                    p = v
        
        total = total + p
print(total)
