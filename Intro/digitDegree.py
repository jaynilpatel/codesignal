def digitDegree(n):
    n_times = 0
    while True:
        if len(str(n)) == 1:
            break
        else:
            li = list(str(n))
            n = 0
            for ch in li:
                n += int(ch)
            n_times += 1
    return n_times

n = 304
print(digitDegree(n))
