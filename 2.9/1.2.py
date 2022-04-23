f = open('1.txt', 'r')
sum = 0
for line in f:
    sum += int(line)

print(sum)
