nums = []
s = []
s1 = []
s2 = []
s3 = []
operations = ''
soperations = []
colscore = []
total= 0
with open('input.txt','r') as file:
    for line in file:
        nums.append(line)
with open('input2.txt','r') as file:
    operations = file.read()
curr,curr1,curr2,curr3 = '','','',''
for i in range(len(nums[0])-1):
    if nums[0][i] != ' ' or nums[1][i] != ' ' or nums[2][i] != ' ' or nums[3][i] != ' ':
        curr = curr + nums[0][i]
        curr1 = curr1 + nums[1][i]
        curr2 = curr2 + nums[2][i]
        curr3 = curr3 + nums[3][i]
    else:
        s.append(curr)
        s1.append(curr1)
        s2.append(curr2)
        s3.append(curr3)
        curr,curr1,curr2,curr3 = '','','',''
s.append(curr)
s1.append(curr1)
s2.append(curr2)
s3.append(curr3)
soperations = operations.split()
for c in range(len(s)):
    if soperations[c] == '+':
        ltotal = 0
    else:
        ltotal = 1
    for i in range(len(s[c])-1,-1,-1):
        num = ''
        if s[c][i].isnumeric():
            num = num + s[c][i]
        if s1[c][i].isnumeric():
            num = num + s1[c][i]
        if s2[c][i].isnumeric():
            num = num + s2[c][i]
        if s3[c][i].isnumeric():
            num = num + s3[c][i]
        pnum = int(num)
        if soperations[c] == '+':
            ltotal += pnum
        else:
            ltotal = ltotal * pnum
    total += ltotal
print(total)
