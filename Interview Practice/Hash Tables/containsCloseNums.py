def containsCloseNums(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d.keys():
            d[nums[i]] = [i]
        else:
            d[nums[i]].append(i)
    print(d)
    for val in d.keys():
        if len(d[val]) > 1:
            for i in range(len(d[val])-1):
                if d[val][i+1]  - d[val][i] <= k:
                    return True
    return False

nums = [0, 1, 2, 3, 5, 2]
k = 2
print(containsCloseNums(nums, k))