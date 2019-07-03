def arrayMaxConsecutiveSum(inputArray, k):
    s0 = sum(inputArray[:k])
    s1 = s0
    for i in range(1,len(inputArray) - k + 1):
        s1 = s1 - inputArray[i-1] + inputArray[i+k-1]
        if s1 > s0: s0 = s1
    return s0

# def arrayMaxConsecutiveSum(inputArray, k):
#     l = len(inputArray) - k + 1
#     return max([sum(inputArray[i:i+k]) for i in range(l)])

inputArray = [2, 3, 5, 1, 6]
k = 2
print(arrayMaxConsecutiveSum(inputArray, k))
