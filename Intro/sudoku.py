grid1 = [0,0,0,0,0,0,0,0,0]
grid2 = [0,0,0,0,0,0,0,0,0]
grid3 = [0,0,0,0,0,0,0,0,0]

grid4 = [0,0,0,0,0,0,0,0,0]
grid5 = [0,0,0,0,0,0,0,0,0]
grid6 = [0,0,0,0,0,0,0,0,0]

grid7 = [0,0,0,0,0,0,0,0,0]
grid8 = [0,0,0,0,0,0,0,0,0]
grid9 = [0,0,0,0,0,0,0,0,0]

def checkList(li):
    l = [0,0,0,0,0,0,0,0,0]
    for i in li:
        if i != '.':
            if l[int(i)-1] == 1:
                return False
            else:
                l[int(i)-1] = 1
    return True

def checkGrid(li, element):
    if(li[int(element)-1] == 1):
        return False
    else:       
        li[int(element)-1] += 1
        return True

def sudoku(grid):
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j] != '.':
                if i<3 and j<3:
                    if not checkGrid(grid1, grid[i][j]):
                        return False
                elif i<3 and j<6:
                    if not checkGrid(grid2, grid[i][j]):
                        return False
                elif i<3 and j<9:
                    if not checkGrid(grid3, grid[i][j]):
                        return False
                elif i<6 and j<3:
                    if not checkGrid(grid4, grid[i][j]):
                        return False
                elif i<6 and j<6:
                    if not checkGrid(grid5, grid[i][j]):
                        return False
                elif i<6 and j<9:
                    if not checkGrid(grid6, grid[i][j]):
                        return False
                elif i<9 and j<3:
                    if not checkGrid(grid7, grid[i][j]):
                        return False
                elif i<9 and j<6:
                    if not checkGrid(grid8, grid[i][j]):
                        return False
                elif i<9 and j<9:
                    if not checkGrid(grid9, grid[i][j]):
                        return False

    for i in range(0,9):
        if not checkList(grid[i]):
            return False
        li = [grid[j][i] for j in range(0,9)]
        if not checkList(li):
            return False
    return True
            

grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]


ans = sudoku(grid)
print(ans)
