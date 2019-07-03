import re
def longestDigitsPrefix(inputString):
    l = [num for num in re.findall(r"^[0-9]+", inputString)]
    longest = ""
    for num in l:
        if len(num) > len(longest):
            longest = num
    return longest

inputString = "123aa1"   
#inputString = "  3 always check for whitespaces 34"
#inputString = "aaaaaaa"
#inputString = "the output is 42"
print(longestDigitsPrefix(inputString))