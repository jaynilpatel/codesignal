def avoidObstacles(inputArray):
    for i in range(2, max(inputArray)):
        f = 0
        for obs in inputArray:
            if obs % i == 0:
                f = 1
        if f == 0:
            return i
    return max(inputArray)+1

#inputArray = [2, 10, 6, 4, 1]
#inputArray = [5, 3, 6, 7, 9]
inputArray = [2,3]
print(avoidObstacles(inputArray))