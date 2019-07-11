from myLinkedList import LinkedList

def isListPalindrome(l):
    if not l:
        return True
    temp = l
    le = 0
    while temp:
        temp = temp.next
        le = le + 1
    mid = le // 2 
    curr = l
    prev = None
    for _ in range(mid):
        head = curr.next
        curr.next = prev
        prev = curr
        curr = head
    if le % 2 == 1:
        curr = curr.next
    for _ in range(mid):
        if prev.value != curr.value:
            return False
        prev = prev.next
        curr = curr.next
    return True

a = LinkedList()
a.push(1)
a.push(3)
a.push(1)
a.push(3)
a.push(1)


li = a.toList()
print(li)
print(isListPalindrome(a.head))




