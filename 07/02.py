def find_parent(tree, parent):
    for key, value in tree.items():
        if parent in value:
            return find_parent(tree, key)
    return parent


def make_sum(tree, nodes, parent):
    tmp_arr = []
    for i in range(len(tree[parent])):
        if tree.get(tree[parent][i]) is not None:
            tmp_arr.append(make_sum(tree, nodes, tree[parent][i]) + nodes[tree[parent][i]])
        else:
            tmp_arr.append(nodes[tree[parent][i]])
    if len(list(set(tmp_arr))) == 1:
        return sum(tmp_arr)
    else:
        for j in range(len(tmp_arr)):
            if tmp_arr.count(tmp_arr[j]) == 1:
                if tmp_arr[j] > min(tmp_arr):
                    print(nodes[tree[parent][j]] - abs(max(tmp_arr) - min(tmp_arr)))
                    exit()

                print(nodes[tree[parent][j]] + abs(max(tmp_arr) - min(tmp_arr)))
                exit()


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
make_sum(tree, nodes, find_parent(tree, parent))
