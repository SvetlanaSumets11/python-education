"""This module to implement the stack"""

from linked_list import LinkedListNode

class Stack:
    """This stack class"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Checking if a list is empty"""
        return self.head is None

    def __len__(self):
        current, ind = self.head, 0
        while current is not None:
            current = current.next
            ind += 1
        return ind

    def push(self, value):
        """Method for adding a node to the list"""
        node = LinkedListNode(value)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        """Remove stack node"""
        if self.is_empty():
            print("Стек пуст")
        else:
            self.head = self.head.next

    def peek(self):
        """Stack node view method"""
        if self.is_empty():
            print("Стек пуст")
        else:
            return self.head.value

    def __str__(self):
        curr = self.head
        string = ''
        while curr is not None:
            string += str(curr.value)
            string +=' -> '
            curr = curr.next
        string += 'None'
        return string

# stack = Stack()
# stack.push(3)
# stack.push(12)
# print(stack.peek())
# print(len(stack))
# print(stack)
# stack.pop()
# print(stack)
