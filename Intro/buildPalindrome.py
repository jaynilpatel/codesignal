def ispalindrome(st):
    return st == st[::-1]

def buildPalindrome(st):
    if st == st[::-1]:
        return st
    else:
        rev_st = st[::-1]
        for i in range(1, len(rev_st)):
            palin_st = st + rev_st[-i::]
            if ispalindrome(palin_st):
                break
    return palin_st

st = "abcdc"
print(buildPalindrome(st))