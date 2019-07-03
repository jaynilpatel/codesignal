def allLongestStrings(inputArray):
    maxLength = 0
    maxStrings = []
    for string in inputArray:
        if len(string) > maxLength:
            maxLength = len(string)
            maxStrings = []
            maxStrings.append(string)
        elif len(string) == maxLength:
            maxStrings.append(string)
    return maxStrings


inputArray= ["abc", "eeee", "abcd", "dcd"]
print(allLongestStrings(inputArray))

