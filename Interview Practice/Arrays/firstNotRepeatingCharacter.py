def firstNotRepeatingCharacter(s):
    b={}
    le1 = len(s)
    le2 = len(b)
    for i,ch in enumerate(s):
        if ch in b:
            b.update({ch:b[ch]+1})
        else:
            b.update({ch:1})
    print(b, type(b))
    x=b.keys()
    y=key=(lambda k: b[k])
    #print(min(x,y))
    ans = min(b, key=b.get)
    if(b[ans] == 1):
        return ans
    else:
        return '_'