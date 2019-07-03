def extractEachKth(inputArray, k):
    del(inputArray[k-1::k])
    return inputArray

inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(extractEachKth(inputArray, k))