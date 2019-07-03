def reverseString(s, start,end):
    print(s[:start] + s[start+1: end][::-1] + s[end+1:] )
    return s[:start] + s[start+1: end][::-1] + s[end+1:] 

def reverseInParentheses(inputString):
    end = -1
    para_pos = []
    for i,ch in enumerate(inputString):
        if ch  == '(':
            para_pos.append([i])
            end += 1
        elif ch == ')':
            x = end
            while (len(para_pos[x]) == 2):
                x -= 1
            para_pos[x].append(i)
    para_pos = para_pos[::-1]
    for i,pos in enumerate(para_pos):
        if i == 0:
            inputString = reverseString(inputString, pos[0], pos[1])
        elif pos[1] > para_pos[i-1][0]:
            a = 1
            while a<=i and (pos[1] > para_pos[i-a][0]):
                a += 1
            a = a-1
            print(a,i)
            inputString = reverseString(inputString, pos[0], pos[1]-(a*2))
        else:
            inputString = reverseString(inputString, pos[0], pos[1])
    return inputString

inputString = "q(wer)t(yui)op"
print(reverseInParentheses(inputString))

inputString = "q(w(iska(jd)e)r)t(yui)op"
print(reverseInParentheses(inputString))

inputString = "q(w(er)ty(us(as)di)o)p"
print(reverseInParentheses(inputString))
