# crypt: ["SEND", 
#  "MORE", 
#  "MONEY"]
# solution: [["O","0"], 
#  ["M","1"], 
#  ["Y","2"], 
#  ["E","5"], 
#  ["N","6"], 
#  ["D","7"], 
#  ["R","8"], 
#  ["S","9"]]

# 9567 + 1085 = 10652

# crypt = ["TEN", "TWO", "ONE"]

# solution = [['O', '1'],
#             ['T', '0'],
#             ['W', '9'],
#             ['E', '5'],
#             ['N', '4']]

# Even though 054 + 091 = 145, 054 and 091

def isCryptSolution(crypt, solution):
    sol = {}
    for i in range(len(solution)):
        sol[solution[i][0]] = solution[i][1]
    print(sol)
    nums=[]
    for string in crypt:
        num = ""
        for ch in string:
            no = sol[ch]
            if no == '0' and len(num) == 0 and len(string) > 1:
               return False
            else:
                num += no
        nums.append(int(num))
    #print(nums)
    if (nums[0] + nums[1]) == nums[2]:
        return True
    else:
        return False




crypt = ["TEN", "TWO", "ONE"]
solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]

# crypt= ["SEND","MORE", "MONEY"]
# solution= [["O","0"], 
#  ["M","1"], 
#  ["Y","2"], 
#  ["E","5"], 
#  ["N","6"], 
#  ["D","7"], 
#  ["R","8"], 
#  ["S","9"]]
crypt= ["A", 
 "A", 
 "A"]
solution= [["A","0"]]

print(isCryptSolution(crypt, solution))