def differentSquares(matrix):
    total2x2 = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            temp = [matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]]
            if temp not in total2x2:
                total2x2.append(temp)   
    return len(total2x2)

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]


print(differentSquares(matrix))