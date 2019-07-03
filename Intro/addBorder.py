def addBorder(picture):
    top = len(picture[0])+2
    
    new_picture = ["*"*top]
    for string in picture:
        new_string = "*" + string + "*"
        new_picture.append(new_string)
    new_picture.append("*"*top)
    return new_picture

picture= ["abcde", 
 "fghij", 
 "klmno", 
 "pqrst", 
 "uvwxy"]

print(addBorder(picture))
