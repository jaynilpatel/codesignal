def rotateMatrix(a):
    size = len(a)
    for layer in range(int(size/2)):
        first = layer
        last = size-layer-1
        for i in range(first,last):
            o = i-first
            temp = a[first][i]
            a[first][i] = a[last-o][first]
            a[last-o][first] = a[last][last-o]
            a[last][last-o] = a[i][last]
            a[i][last]= temp

    return a

a = [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]

b = rotateMatrix(a)
print(b)