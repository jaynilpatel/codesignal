def bishopAndPawn(bishop, pawn):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row_b = int(bishop[1])
    col_b = alpha.index(bishop[0]) + 1
    row_p = int(pawn[1])
    col_p = alpha.index(pawn[0]) + 1
    diff_b = abs(row_b - row_p)
    diff_p = abs(col_b - col_p)
    return diff_b == diff_p
    


bishop = "g1"
pawn = "f3"
print(bishopAndPawn(bishop, pawn))