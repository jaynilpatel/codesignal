def matrixElementsSum(matrix):
    haunted = []
    sum = 0
    for i in range(0, len(matrix)):
        for j in range(0 ,len(matrix[i])):
            if j not in haunted:
                if matrix[i][j] == 0:
                    haunted.append(j)
                else:
                    sum = sum + matrix[i][j]

    return sum

matrix = [[0,1],
          [2,0]]

print(matrixElementsSum(matrix))