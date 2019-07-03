def chessBoardCellColor(cell1, cell2):
    alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    row1,col1 = alpha_list.index(cell1[0]), int(cell1[1])-1
    row2,col2 = alpha_list.index(cell2[0]), int(cell2[1])-1
    if row1 % 2 == 0:
        if col1 % 2 == 0:
            color1 = "black"
        else:
            color1 = "white"
    else:
        if col1 % 2 == 0:
            color1 = "white"
        else:
            color1 = "black"

    if row2 % 2 == 0:
        if col2 % 2 == 0:
            color2 = "black"
        else:
            color2 = "white"
    else:
        if col2 % 2 == 0:
            color2 = "white"
        else:
            color2 = "black"

    return color1 == color2

cell1 = "H8"
cell2 = "H3"
print(chessBoardCellColor(cell1, cell2))