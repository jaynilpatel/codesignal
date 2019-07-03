def findEmailDomain(address):
    return address.split("@")[-1]



address= "someaddress@yandex.ru"
print(findEmailDomain(address))