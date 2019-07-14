# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def addTwoHugeNumbers(a, b):
    temp_a = a
    temp_b = b
    str_a, str_b = "", ""
    while temp_a:
        str_a += str(temp_a.value).zfill(4)
        temp_a = temp_a.next
    while temp_b:
        str_b += str(temp_b.value).zfill(4)
        temp_b = temp_b.next
    c = str(int(str_a) + int(str_b))
    c = c[::-1]
    c = [int(c[0+i:4+i][::-1]) for i in range(0, len(c), 4)][::-1]
    result = ListNode(c[0])
    head = result
    for val in c[1:]:
        new_node = ListNode(val)
        result.next = new_node
        result = new_node
    return head
