def lineEncoding(s):
    subList = []
    sub = ""
    for i in range(0,len(s)):
        if i == 0:
            sub += s[i]
        else:
            if s[i] == s[i-1]:
                sub += s[i]
            else:
                subList.append(sub)
                sub = s[i]
    subList.append(sub)
    new_s = ""
    for sub in subList:
        if len(sub) > 1:
            new_s += str(len(sub)) + sub[0]
        else:
            new_s += sub[0]
    return new_s

s = "aabbbcaa"
#s = "wwwwwwwawwwwwww"
print(lineEncoding(s))