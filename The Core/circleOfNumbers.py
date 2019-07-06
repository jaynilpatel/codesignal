def circleOfNumbers(n, firstNumber):
    return (((n // 2)) + firstNumber) % n


n, firstNumber = 18, 6

print(circleOfNumbers(n, firstNumber))