def deleteDigit(n):
    possible_nos = []
    n = str(n)
    for i in range(len(n)):
        possible_nos.append(int(n[0:i]+n[i+1:]))
    return max(possible_nos)


n = 152
print(deleteDigit(n))