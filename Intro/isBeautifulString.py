def isBeautifulString(inputString):
    count = [0]*26
    for ch in inputString:
        count[ord(ch)-97] += 1
    return count == sorted(count, reverse=True)
    


inputString = "bbbaacdafe"
print(isBeautifulString(inputString))