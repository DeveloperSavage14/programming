def recurse(index, t, b):
    key = (index, tuple(t))
    if key in memo:
        return memo[key]
    if index == len(b) - 1:
        btn = b[index]
        if index == len(b) - 1:
            btn = b[index]
        p = -1
        for k in range(len(btn)):
            if btn[k] != 0:
                p = k
                break

        if p == -1:
            zero = True
            for val in t:
                if val != 0:
                    zero = False
                    break

            if zero:
                return 0
            else:
                return float('inf')

        if t[p] % btn[p] != 0:
            return float('inf')
        
        presses = t[p] // btn[p]
        if presses < 0:
            return float('inf')

        for i in range(len(t)):
            if t[i] != (presses * btn[i]):
                return float('inf')
                
        return presses
    cb = b[index] 
    limit = float('inf')
    for i in range(len(t)):
        if cb[i] > 0:
            p = t[i] // cb[i]
            if p < limit:
                limit = p
    if limit == float('inf'):
        limit = 0 
    besttotal = float('inf')
    for c in range(limit + 1):
        nexttargets = []
        possible = True
        
        for k in range(len(t)):
            rem = t[k] - (c * cb[k])
            if rem < 0:
                possible = False
                break
            nexttargets.append(rem)
            
        if possible:
            r = recurse(index + 1, nexttargets, b)
            
            if r != float('inf'):
                total = c + r
                if total < besttotal:
                    besttotal = total
    memo[key] = besttotal
    return besttotal
buttons = []
jolts = []
gtotal = 0
with open('input.txt', 'r') as file:
    for line in file:
        curr = line.strip().split(" ")
        jolts.append(curr[-1][1:-1].split(','))
        curr.pop(0)
        curr.pop(-1)
        buttons.append(curr)
for i in range(len(jolts)):
    memo = {}
    length = len(jolts[i])
    target = []
    base = []
    bases = []
    for c in range(len(jolts[i])):
        target.append(int(jolts[i][c]))
        base.append(0)
    vecb = []
    for c in range(len(buttons[i])):
        buts = buttons[i][c].strip('()').split(",")
        temp = []
        for m in base:
            temp.append(m)
        for t in buts:
            temp[int(t)] = 1
        vecb.append(temp)
    ans = recurse(0,target, vecb)
    gtotal += ans
print(gtotal)
        
