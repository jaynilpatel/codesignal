def rotateImage(a):
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
