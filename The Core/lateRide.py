def lateRide(n):
    hrs = list(str(n//60))
    mi = list(str(n%60))
    total = 0
    for i in hrs:
        total = total + int(i)
    for i in mi:
        total = total + int(i)
    return total

n = 240
print(lateRide(n))