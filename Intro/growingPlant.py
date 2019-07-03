def growingPlant(upSpeed, downSpeed, desiredHeight):
    days, plantHeight = 0, 0
    while True:
        days += 1
        plantHeight += upSpeed
        if plantHeight >= desiredHeight:
            break
        plantHeight -= downSpeed
    return days

upSpeed = 100
downSpeed = 10
desiredHeight = 910
print(growingPlant(upSpeed, downSpeed, desiredHeight))