def addTwoDigits(n):
    return sum([int(str(n)[0]), int(str(n)[1])])

n = 98
print(addTwoDigits(n))