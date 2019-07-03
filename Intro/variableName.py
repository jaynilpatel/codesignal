import re

def variableName(name):
    regex = re.compile(r'^[a-zA-Z_$][a-zA-Z_$0-9]*$')
    if regex.match(name) == None:
        return False
    else:
        return True

name = "qqq"
print(variableName(name))