from math import sqrt

n = int(input())
tmp = 0
n1 = int(sqrt(n))
if n1 != sqrt(n):
    n1 += 1
if n1 % 2 != 1:
    n1 += 1
to_center = n1 // 2
for i in range(4):
    arr = [x for x in range(n1**2 - ((n1 - 1) * i), (n1**2 - n1) - ((n1 - 1) * i), -1)]
    if n in arr:
        print(to_center + (abs(n - arr[n1 // 2])))
        exit()
