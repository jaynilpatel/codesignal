def areFollowingPatterns(strings, patterns):
    d = {}
    for i in range(len(strings)):
        if strings[i] in d.keys():
            if patterns[i] != d[strings[i]]:
                return False
        elif patterns[i] in d.values():
            return False
        else:
            d[strings[i]] = patterns[i]
    return True

strings = ["cat", "dog", "cat"]  
patterns = ["a", "b", "b"]

# strings = ["cat", "dog", "doggy"]  
# patterns = ["a", "b", "b"]

print(areFollowingPatterns(strings, patterns))