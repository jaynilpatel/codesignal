# grid: 
# [[".",".",".","1","4",".",".","2","."], 
#  [".",".","6",".",".",".",".",".","."], 
#  [".",".",".",".",".",".",".",".","."], 
#  [".",".","1",".",".",".",".",".","."], 
#  [".","6","7",".",".",".",".",".","9"], 
#  [".",".",".",".",".",".","8","1","."], 
#  [".","3",".",".",".",".",".",".","6"], 
#  [".",".",".",".",".","7",".",".","."], 
#  [".",".",".","5",".",".",".","7","."]]

# OP: true

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

def sudoku2(grid):
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
            

grid =[[".",".",".","1","4",".",".","2","."], 
 [".",".","6",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".","1",".",".",".",".",".","."], 
 [".","6","7",".",".",".",".",".","9"], 
 [".",".",".",".",".",".","8","1","."], 
 [".","3",".",".",".",".",".",".","6"], 
 [".",".",".",".",".","7",".",".","."], 
 [".",".",".","5",".",".",".","7","."]] 


ans = sudoku2(grid)
print(ans)

# print("Grid1:", grid1)
# print("Grid2:", grid2)
# print("Grid3:", grid3)
# print("Grid4:", grid4)
# print("Grid5:", grid5)
# print("Grid6:", grid6)
# print("Grid7:", grid7)
# print("Grid8:", grid8)
# print("Grid9:", grid9)
