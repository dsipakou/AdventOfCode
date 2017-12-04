input_str = str(input())
output = 0
for i in range(len(input_str) - 1):
    if input_str[i] == input_str[i + 1]:
        output += int(input_str[i])
if input_str[0] == input_str[len(input_str) - 1]:
    output += int(input_str[0])
print(output)