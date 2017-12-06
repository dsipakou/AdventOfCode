arr = list(map(int, input().split()))
dublicate = False
output = 0
tmp_arr = []
while not dublicate:
    number = max(arr)
    index = arr.index(number)
    arr[index] = 0
    for i in range(number):
        arr[(index + i + 1) % len(arr)] += 1
    if arr not in tmp_arr:
        tmp_arr.append([x for x in arr])
    else:
        dublicate = True
        output = abs(tmp_arr.index(arr) - len(tmp_arr))

print(output)