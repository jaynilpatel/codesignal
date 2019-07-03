def stringsRearrangement(inputArray):
    used = [False] * len(inputArray)
    findPermutation(inputArray, None, used ,0)
    global success
    return success

def findPermutation(a, prev, used, n):
    if n == len(a):
        global success
        success = True
        #print("Success:",success)
        return
    
    for i in range(0, len(a)):
        if (not used[i]) and (prev == None or differOne(a[i], prev)):
            #print(a[i])
            used[i] = True
            findPermutation(a, a[i], used, n+1)
            used[i] = False

def differOne(a, b):
    c = 0
    #print(a,b)
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
            #print("c:",c)
            if c > 1:
                return False
    return c == 1  

success = False

inputArray = ["aba", "bbb", "bab"]

#inputArray = ["ab", "bb", "aa"]
#print("inputArray:", inputArray)
print(stringsRearrangement(inputArray))
