def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft in [friendsLeft, friendsRight]) and (yourRight in [friendsLeft, friendsRight]) 


yourLeft= 1
yourRight= 10
friendsLeft= 10
friendsRight= 0

print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))