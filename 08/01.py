vals = {}

def comparing(operator, val1, val2):
    if operator == '>':
        return vals[val1] > int(val2)
    elif operator == '<':
        return vals[val1] < int(val2)
    elif operator == '==':
        return vals[val1] == int(val2)
    elif operator == '!=':
        return vals[val1] != int(val2)
    elif operator == '>=':
        return vals[val1] >= int(val2)
    elif operator == '<=':
        return vals[val1] <= int(val2)
    return False

def ar(operator, val1, val2):
    if operator == 'inc':
        return val1 + int(val2)
    elif operator == 'dec':
        return val1 - int(val2)

line = input()

while line:
    cond = False
    arr = line.split(' ')
    vals[arr[0]] = vals.get(arr[0], 0)
    vals[arr[4]] = vals.get(arr[4], 0)
    cond = comparing(arr[5], arr[4], arr[6])
    if cond:
        vals[arr[0]] = ar(arr[1], vals[arr[0]], arr[2])
    line = input()
print(vals)
print(max(vals.values()))