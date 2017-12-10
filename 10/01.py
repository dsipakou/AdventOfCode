from itertools import cycle

arr = [x for x in range(256)]

l = list(map(int, input().split(',')))

current_position = 0
skip = 0

for i in range(len(l)):
    num = l[i]
    reversed_arr = [arr[x % len(arr)] for x in range(current_position, current_position + num)][::-1]
    for j in range(len(reversed_arr)):
        arr[(j + current_position) % len(arr)] = reversed_arr[j]
    print(arr)
    current_position += num + skip
    skip += 1
print(arr[0] * arr[1])
