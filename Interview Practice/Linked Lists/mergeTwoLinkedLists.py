from myLinkedList import LinkedList
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def mergeTwoLinkedLists(l1, l2):
    if not l1 and not l2:
        return None
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.value  > l2.value:
        l3 = ListNode(l2.value)
        l2 = l2.next
    else:
        l3 = ListNode(l1.value)
        l1 = l1.next
    
    l3_head = l3

    while l1 and l2:
        if l1.value  > l2.value:
            curr = ListNode(l2.value)
            l2 = l2.next
            l3.next = curr 
        else:
            curr = ListNode(l1.value)
            l1 = l1.next 
            l3.next = curr
        l3 = curr
        
    while l1:
        curr = ListNode(l1.value)
        l1 = l1.next 
        l3.next = curr
        l3 = curr
        
    while l2:
        curr = ListNode(l2.value)
        l2 = l2.next 
        l3.next = curr
        l3 = curr
        
    return l3_head
        
        

l1 = LinkedList()
l1.push(4)
l1.push(2)
l1.push(1)
l1.push(1)

l2 = LinkedList()
l2.push(5)
l2.push(3)
l2.push(0)

print(mergeTwoLinkedLists(l1.head, l2.head))