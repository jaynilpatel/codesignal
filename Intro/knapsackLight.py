def knapsackLight(value1, weight1, value2, weight2, maxW):
    maxVal1, maxVal2, maxVal12 = 0,0,0
    if weight1 <= maxW:
        maxVal1 = value1 
    if weight2 <= maxW:
        maxVal2 = value2
    if weight1 + weight2 <= maxW:
        maxVal12 = value1 + value2
    return max(maxVal1, maxVal2, maxVal12)


value1 = 15
weight1 = 2
value2 = 20
weight2 = 3
maxW = 2

print(knapsackLight(value1, weight1, value2, weight2, maxW))