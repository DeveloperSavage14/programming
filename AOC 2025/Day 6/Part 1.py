nums = ''
snums = []
operations = ''
soperations = []
colscore = []
total= 0
with open('input.txt','r') as file:
    nums = file.read()
with open('input2.txt','r') as file:
    operations = file.read()
snums = nums.split()
soperations = operations.split()
for i in range(len(soperations)):
    if soperations[i] == '+':
        total += int(snums[i]) + int(snums[i+1000]) + int(snums[i+2000]) + int(snums[i+3000])
    else:
        total += int(snums[i]) * int(snums[i+1000]) * int(snums[i+2000]) * int(snums[i+3000])
print(total)
