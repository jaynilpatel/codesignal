def arrayMaximalAdjacentDifference(inputArray):
    max = -30
    for i in range(0, len(inputArray)-1):
        if max < abs(inputArray[i] - inputArray[i+1]):
            max = abs(inputArray[i] - inputArray[i+1])
    return max

inputArray = [2, 4, 1, 0]
print(arrayMaximalAdjacentDifference(inputArray))