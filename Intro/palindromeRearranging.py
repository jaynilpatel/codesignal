def palindromeRearranging(inputString):
    alphabet = [0]*26
    length = len(inputString)
    for i in inputString:
        index = ord(i) - 97
        alphabet[index] += 1
    print(alphabet)
    f = 0
    if length % 2 == 1:
        f = 1
    for i in alphabet:
        if i % 2 == 1:
            if f == 1:
                f = 0
            else:
                return False
    return True
         

#inputString = "aabb"
inputString= "abbcaaabb"
print(palindromeRearranging(inputString))