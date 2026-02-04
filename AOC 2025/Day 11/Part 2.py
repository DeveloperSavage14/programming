codes = {}
visited = []
with open('input.txt','r') as file:
    for line in file:
        code = line[:3]
        code1 = line[4:].strip().split(' ')
        codes[code] = []
        for i in code1:
            codes[code].append(i)


def win(thing,part,wpaths):
    if thing in wpaths:
        return wpaths[thing]
    if thing == part:
        return 1
    if thing not in codes:
        return 0
    total = 0
    for p in codes[thing]:
        total += win(p,part,wpaths)
    wpaths[thing] = total
    return total
step = win('svr','dac',{})
step2 = win('dac','fft',{})
step3 = win('fft','out',{})
tot1 = step * step2 * step3
steps = win('svr','fft',{})
steps2 = win('fft','dac',{})
steps3 = win('dac','out',{})
tot2 = steps * steps2 * steps3
print(tot1 + tot2)
