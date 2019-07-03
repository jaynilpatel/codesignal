def firstDigit(inputString):
    for i in inputString:
        if i.isdigit():
            return i


inputString = "var_1__Int"
print(firstDigit(inputString))