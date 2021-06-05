"""This is a module for implementing a queue"""

from linked_list import LinkedListNode

class Queue:
    """This is the queue class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """Checking if a queue is empty"""
        return self.head is None

    def __len__(self):
        current, ind = self.head, 0
        while current is not None:
            current = current.next
            ind += 1
        return ind

    def enqueue(self, value):
        """Method for adding a node to the end of the queue"""
        node = LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        """Method for retrieval a node to the end of the queue"""
        if self.is_empty():
            print("Очередь пуста")
        else:
            self.head = self.head.next

    def peek_head(self):
        """View the head of the queue"""
        if self.is_empty():
            print("Очередь пуста")
        else:
            return self.head.value

    def peek_tail(self):
        """View the tail of the queue"""
        if self.is_empty():
            print("Очередь пуста")
        else:
            return self.tail.value

    def __str__(self):
        curr = self.head
        string = ''
        while curr is not None:
            string += str(curr.value)
            string +=' -> '
            curr = curr.next
        string += 'None'
        return string


# queue = Queue()
# queue.enqueue(3)
# queue.enqueue(12)
# print(queue.peek_head())
# print(queue.peek_tail())
# print(len(queue))
# print(queue)
# queue.dequeue()
# print(queue)
