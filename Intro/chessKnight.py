def chessKnight(cell):
    row = ord(cell[0]) - 96
    col = int(cell[1])
    pos = [(row+2,col+1),(row+2,col-1),(row-2,col+1),(row-2,col-1),
           (row+1,col+2),(row+1,col-2),(row-1,col+2),(row-1,col-2)]
    return sum([1 for row,col in pos if (row > 0 and row < 9) and (col > 0 and col < 9) ])
cell = "d5"
print(chessKnight(cell))