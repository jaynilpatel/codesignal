def minesweeper(matrix):
    new_matrix = [[False] * (len(matrix[0]) + 2)]
    for li in matrix:
        new_li = [False] + li + [False]
        new_matrix.append(new_li)
    new_matrix.append([False] * (len(matrix[0]) + 2))
    output = []
    for i in range(1, len(matrix)+1):
        row = []
        for j in range(1, len(matrix[0])+1):
            total = 0
            total += new_matrix[i-1][j-1]
            total += new_matrix[i-1][j]
            total += new_matrix[i-1][j+1]

            total += new_matrix[i][j-1]
            total += new_matrix[i][j+1]

            total += new_matrix[i+1][j-1]
            total += new_matrix[i+1][j]
            total += new_matrix[i+1][j+1]
            row.append(total)
        output.append(row)
    return(output)

matrix = [[True,False,False,True], 
        [False,False,True,False], 
        [True,True,False,True]]

print(minesweeper(matrix))