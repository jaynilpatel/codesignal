def firstDuplicate(a):
    b = set({})
    l = len(a)
    min = [-1,l+1]
    l2 = len(b)
    for i,ele in enumerate(a):
        b.add(ele)
        temp = len(b)
        if l2 == temp:
            if min[1]>i:
                min[1] = i
                min[0] = ele
        else:
            l2 = temp
            
    if(l+1 == min[1]):
        return -1
    return min[0]