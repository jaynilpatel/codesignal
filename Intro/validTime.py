def validTime(time):
    timeList = time.split(":")
    hr = int(timeList[0])
    mi = int(timeList[1])
    return hr>=0 and hr<24 and mi>=0 and mi <60

time = "13:58"
#time = "25:51"
print(validTime(time))