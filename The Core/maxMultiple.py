def maxMultiple(divisor, bound):
    while bound % divisor != 0:
        bound = bound - 1
    return bound


divisor = 3
bound = 10
print(maxMultiple(divisor, bound))