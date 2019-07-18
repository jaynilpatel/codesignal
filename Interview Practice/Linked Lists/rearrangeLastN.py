# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def rearrangeLastN(l, n):
    if n == 0:
        return l
    temp = l
    le = 0
    while temp:
        le = le + 1
        temp = temp.next
    if n == le:
        return l
    curr = l
    for _ in range(le-n):
        prev1 = curr
        curr = curr.next
    prev1.next = None
    head = curr
    while curr:
        prev2 = curr
        curr = curr.next
    prev2.next,l = l, head
    temp = l
    while temp:
        print(temp.value)
        temp = temp.next
    return l
    

# l = [1, 2, 3, 4, 5] , n=3

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
n = 0

rearrangeLastN(l, n)
