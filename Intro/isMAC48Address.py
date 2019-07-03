def isMAC48Address(inputString):
    groups = inputString.split("-")
    if len(groups) == 6:
        for group in groups:
            if len(group) == 2:
                if not ((ord(group[0]) >= 48 and ord(group[0]) <= 57) or (ord(group[0]) >= 65 and ord(group[0]) <= 70)):
                    return False
                if not ((ord(group[1]) >= 48 and ord(group[1]) <= 57) or (ord(group[1]) >= 65 and ord(group[1]) <= 70)):
                    return False
            else:
                return False
        return True
    else:
        return False

inputString = "00-1B-63-84-45-E6"
#tString = "Z1-1B-63-84-45-E6"

print(isMAC48Address(inputString))