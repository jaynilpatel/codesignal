def isIPv4Address(inputString):
    ipList = inputString.split(".")
    if len(ipList) == 4:
        for i in ipList:
            if i.isdigit():
                if int(i) < 0 or int(i) > 255:
                    return False
            else:
                return False
        return True
    else:
        return False


# inputString = "172.16.254.1"
# inputString = "172.316.254.1"
inputString = ".254.255.0"
print(isIPv4Address(inputString))