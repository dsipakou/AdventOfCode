output = 0
line = input()
while line:
    arr = [int(x) for x in line.split()]
    output += abs(min(arr) - max(arr))
    line = input()
print(output)