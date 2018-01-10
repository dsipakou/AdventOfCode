line = input()
arr = []
while line:
    arr.append(int(line))
    line = input()

inside = True
output = 0
current_index = 0
# while inside:
#     cur = arr[current_index]
#     arr[current_index] += 1
#     output += 1
#     current_index += cur
#     if current_index < 0 or current_index > len(arr) - 1:
#         inside = False
# print(output)
while inside:
    cur = arr[current_index]
    if cur >= 3:
        arr[current_index] -= 1
    else:
        arr[current_index] += 1
    output += 1
    current_index += cur
    if current_index < 0 or current_index > len(arr) - 1:
        inside = False
print(output)
