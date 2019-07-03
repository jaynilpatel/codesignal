def arrayChange(inputArray):
    moves = 0
    for i in range(1, len(inputArray)):
        if inputArray[i-1] >= inputArray[i]:
            move = (inputArray[i-1] - inputArray[i]) + 1 
            moves += move
            inputArray[i] += move
            
    return moves


inputArray = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
print(arrayChange(inputArray))