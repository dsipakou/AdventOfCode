def find_parent(tree, parent):
    for key, value in tree.items():
        if parent in value:
            return find_parent(tree, key)

    return parent

line = input()
arr = []
while line:
    arr.append(line)
    line = input()
tree = {}
parent = ''
for i in range(len(arr)):
    if arr[i].find('->') > 0:
        key = arr[i][:arr[i].index(' ')]
        values = arr[i][arr[i].find('->') + 2:].replace(',', '').split()
        if parent == '':
            parent = key
        tree[key] = values

print(find_parent(tree, parent))

