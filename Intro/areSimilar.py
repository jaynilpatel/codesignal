# def areSimilar(a, b):
#     if len(a) != len(b):
#         return False
#     no_swap = 0
#     for i in range(0, len(a)):
#         if a[i] not in b or b[i] not in a:
#             return False
#         else:
#             # pos = b.index(a[i])
#             if a[i] != b[i]:
#                 if no_swap == 1:
#                     return False
#                 n = True
#                 a_pos = 0
#                 while(n):
#                     a_pos = a[a_pos+1:].index(b[i])
#                     if b[a_pos] == a[i]:
#                         no_swap = 1
#                         b[i],b[a_pos] = b[a_pos], b[i]
#                     elif a[i] not in b[a_pos+1:]:
#                         return False
#    return True


def areSimilar(a, b):
    if len(a) != len(b):
        return False
    swap = []
    f = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            f = 1
            if len(swap) == 2:
                return False
            else:
                swap.append([a[i], b[i]])
    if f == 0:
        return True
    if len(swap) == 2:
        if (swap[0][0] == swap[1][1] and swap[0][1] == swap[1][0]):
            return True
        else:
            return False
    else:
        return False
    

# a = [1, 2, 2, 3]
# b = [2, 2, 2, 3]

a = [1,2,3]
b = [2,4,3]
print(areSimilar(a,b))