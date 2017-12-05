from collections import Counter
output = 0
line = input()
while line:
    tmp = Counter(line.split(' '))
    if sorted(tmp.values(), reverse=True)[0] == 1:
        output += 1
    line = input()
print(output)