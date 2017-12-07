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
nodes = {}
parent = ''
for i in range(len(arr)):
    nodes[arr[i][:arr[i].index(' ')]] = int(arr[i][arr[i].index('(') + 1:arr[i].index(')')])

    if arr[i].find('->') > 0:
        key = arr[i][:arr[i].index(' ')]
        values = arr[i][arr[i].find('->') + 2:].replace(',', '').split()
        if parent == '':
            parent = key
        tree[key] = values
print(nodes)
print(tree)
print(find_parent(tree, parent))


