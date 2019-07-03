def commonCharacterCount(s1, s2):
    commonCount = 0
    s1_list = list(s1)
    for ch in s2:
        if ch in s1_list:
            commonCount += 1
            s1_list[s1_list.index(ch)] = 0
    return commonCount

s1= "aabcc"
s2= "adcaa"
print(commonCharacterCount(s1, s2))
