import re
def longestWord(text):
    wordList = re.findall(r"[a-zA-Z]+", text)
    print(wordList)
    maxLen = 0
    longWord = ""
    for word in wordList:
        if len(word) > maxLen:
            maxLen = len(word)
            longWord = word
    return longWord

text = "Ready, steady, go!"
text = "You are the best!!!!!!!!!!!! CodeFighter ever!"
text = "1234"
print(longestWord(text))