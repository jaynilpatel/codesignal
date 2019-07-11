class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def toList(self):
        temp = self.head
        li = []
        while temp:
            li.append(temp.value)
            temp = temp.next
        return li