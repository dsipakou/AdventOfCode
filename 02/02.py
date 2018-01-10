# output = 0
# line = input()
# while line:
#     arr = [int(x) for x in line.split()]
#     output += abs(min(arr) - max(arr))
#     line = input()
# print(output)

output = 0
line = input()
while line:
    found = False
    arr = [int(x) for x in line.split()]
    for i in range(len(arr) - 1):
        if found:
            break
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                output += 1
            elif arr[i] > arr[j]:
                if arr[i] % arr[j] == 0:
                    output += arr[i] // arr[j]
                    found = True
                    break
            elif arr[j] % arr[i] == 0:
                output += arr[j] // arr[i]
                found = True
                break
    line = input()
print(output)