import re
def sumUpNumbers(inputString):
    nos = re.findall(r"\d+", inputString)
    return sum([int(i) for i in nos])
    

inputString = "2 apples, 12 oranges"
print(sumUpNumbers(inputString))