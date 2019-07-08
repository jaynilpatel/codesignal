# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#   
def removeKFromList(l, k):
    while l and l.value==k:
        l=l.next
    temp = l
    while temp:
        x = temp
        temp = temp.next
        while temp and temp.value == k:
            temp = temp.next
        x.next = temp
        
    return l

l = [1, 2, 3, 4, 5, 6, 7]
k = 10
print(removeKFromList(l,k))