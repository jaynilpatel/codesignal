# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def reverseLinkedList(li, k):
    curr = li
    prev = None
    for _ in range(k):
        head = curr.next
        curr.next = prev
        prev = curr
        curr = head
    return li, prev, curr

def reverseNodesInKGroups(l, k):
    if k < 2:
        return l
    else:
        temp = l
        le = 0
        while temp:
            temp = temp.next
            le += 1
        start = None
        curr = l
        i = 1
        while le >= k:
            if i == 1:
                li, prev, curr = reverseLinkedList(curr, k)
                start = prev
                temp_end = li
            else:
                li, prev, curr = reverseLinkedList(curr, k)  
                temp_end.next = prev
                temp_end = li
            le = le - k
            i = i + 1
        temp_end.next = curr
        temp = start
        while temp:
            print(temp.value)
            temp = temp.next
        return start

# l = [1, 2, 3, 4, 5] , k=2

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
k = 2

reverseNodesInKGroups(l,k)