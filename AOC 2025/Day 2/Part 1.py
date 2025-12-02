with open('input.txt', 'r') as file:
    content = file.read()
    total = 0
    ranges = content.split(',')
    for i in ranges:
        curr = i.split('-')
        for p in range(int(curr[0]),int(curr[1])+1):
            p = str(p)
            if len(p) % 2 == 0:
                if p[:len(p)//2] == p[len(p)//2:]:
                    total = total + int(p)
print(total)
