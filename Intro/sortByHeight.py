def sortByHeight(a):
    index_tree = []
    b = []
    for obj in a:
        if obj == -1:
            index_tree.append(a.index(obj))
            a[a.index(obj)] = -2
        else:
            b.append(obj)
    b = sorted(b)
    x = 0
    for i in range(0, len(a)):
        if a[i] == -2:
            a[i] = -1
        else:
            a[i] = b[x]
            x += 1
    return a


a = [4, 2, 9, 11, 2, 16]
print(sortByHeight(a))