def evenDigitsOnly(n):
    for i in str(n):
        if int(i) % 2 == 1:
            return False
    return True

n = 12345
print(evenDigitsOnly(n))