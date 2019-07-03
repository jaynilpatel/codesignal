def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if elemToReplace == i else i for i in inputArray]
        


inputArray= [1, 2, 1]
elemToReplace= 1
substitutionElem= 3
print(arrayReplace(inputArray, elemToReplace, substitutionElem))