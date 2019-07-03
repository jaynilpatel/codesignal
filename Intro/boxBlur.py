def boxBlur(image):
    max_row = len(image) - 3
    max_col = len(image[0]) - 3
    box_Blur = []
    for i in range(0, max_row+1):
        row = []
        for j in range(0, max_col+1):
            total = sum(image[i][j:j+3])+sum(image[i+1][j:j+3])+sum(image[i+2][j:j+3])
            total = int(total/9)
            row.append(total)
        box_Blur.append(row)
    return box_Blur

# image= [[36,0,18,9,9,45,27], 
#         [27,0,54,9,0,63,90], 
#         [81,63,72,45,18,27,0], 
#         [0,0,9,81,27,18,45], 
#         [45,45,27,27,90,81,72], 
#         [45,18,9,0,9,18,45], 
#         [27,81,36,63,63,72,81]]

# image = [[1, 1, 1], 
#          [1, 7, 1], 
#          [1, 1, 1]]
image= [[36,0,18,9], 
 [27,54,9,0], 
 [81,63,72,45]]
print(boxBlur(image))