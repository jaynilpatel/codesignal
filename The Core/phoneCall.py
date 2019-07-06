def phoneCall(min1, min2_10, min11, s):
    tot_min = 0
    if s < min1:
        return tot_min
    s = s - min1
    tot_min += 1
    for _ in range(2, 11):
        if s < min2_10:
            return tot_min
        else:
            tot_min += 1
            s = s - min2_10
    tot_min = tot_min + (s//min11)
    return tot_min

min1= 1
min2_10= 2
min11= 1
s= 6

print(phoneCall(min1, min2_10, min11, s))