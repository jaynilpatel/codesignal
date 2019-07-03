def alphabeticShift(inputString):
    new_string = ""
    for i in inputString:
        pos = ord(i)
        if pos == 122:
            pos = 97
        else:
            pos = pos +1
        new_string += chr(pos)
    return new_string


inputString = "crazy"
print(alphabeticShift(inputString))