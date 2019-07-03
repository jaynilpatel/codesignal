def getName(fName, arr):
    k = 1 
    while fName+"("+str(k)+")" in arr:
        k = k +1
    return  fName+"("+str(k)+")"

def fileNaming(names):
    for i in range(1, len(names)):
        if names[i] in names[0:i]:
            names[i] = getName(names[i], names[0:i])
    return names

names = ["doc", "doc", "image", "doc(1)", "doc"]
#names = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
print(fileNaming(names))