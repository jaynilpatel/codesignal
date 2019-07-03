def isLucky(n):
    nos = list(str(n))
    sum = 0
    for i in range(0, int(len(nos)/2)):
        sum += int(nos[i])
        sum -= int(nos[len(nos) - 1 - i])
    return not bool(sum)
n= 1230
print(isLucky(n))