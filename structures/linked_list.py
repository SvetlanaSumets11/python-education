"""This module for implementing linked list"""

class LinkedListNode:
    """This is the class of the linked list node"""
    def __init__(self, value, next = None):
        self.value = value
        self.next = None


class LinkedList:
    """This is a linked list class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """Checking if a list is empty"""
        return self.head is None

    def append(self, value):
        """Method for adding a node to the end of the list"""
        node = LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, value):
        """Method for adding a node to the beginning of the list"""
        node = LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def __len__(self):
        if self.is_empty():
            return 0
        current, ind = self.head, 0
        while current is not None:
            current = current.next
            ind += 1
        return ind

    def insert(self, ind_node, value):
        """Method for inserting a node with a specified value
        at a specified index into a list"""
        if ind_node == 0:
            self.prepend(value)
        elif ind_node == len(self):
            self.append(value)
        elif 0 < ind_node < len(self):
            node = LinkedListNode(value)
            ind = 0
            current = self.head
            while current:
                if ind_node == ind + 1:
                    node.next = current.next
                    current.next = node
                current = current.next
                ind += 1
        else:
            raise IndexError ("Индекс вне пределов списка")

    def get(self, ind_node):
        """The method will return the value of the node at the given index"""
        if self.is_empty():
            print("Список пуст")
        if ind_node < 0:
            raise ValueError("Значение индекса меньше 0")
        current = self.head
        ind = 0
        while ind <= ind_node:
            if ind == ind_node:
                return current.value
            if current.next is None and ind < ind_node:
                raise ValueError("Нет узла с таким индексом")
            ind += 1
            current = current.next

    def is_value(self, value):
        """Method for checking the existence of a node with a given value in the list"""
        if self.is_empty():
            print("Список пуст")
        current = self.head
        while current.value != value:
            if current.next is None and current.value != value:
                return False
            current = current.next
        return True

    def delete(self, ind_node):
        """Method for removing a node at a given index from the list"""
        if ind_node < 0:
            raise ValueError("Значение индекса меньше 0")
        if self.is_empty():
            print("Список пуст")
        else:
            current = self.head
            prev = None
            ind = 0
            while ind <= ind_node:
                if ind == ind_node:
                    if current == self.head:
                        self.head = current.next
                    else:
                        prev.next = current.next
                    break
                if current.next is None and ind < ind_node:
                    raise ValueError(f"Нет узла с таким индексом {ind_node}")
                ind += 1
                prev = current
                current = current.next

    def delete_value(self, value):
        """Method for removing a node / nodes by a given value from the list"""
        if self.is_empty():
            print("Список пуст")
        else:
            current = self.head
            ind = 0

            while current is not None:
                if current.value == value:
                    self.delete(ind)
                else:
                    ind += 1
                current = current.next

    def delete_head(self):
        """List head removal method"""
        self.delete(0)

    def delete_tail(self):
        """List tail removal method"""
        self.delete(len(self) - 1)

    def __repr__(self):
        return str(self)

    def __str__(self):
        curr = self.head
        string = ''
        while curr is not None:
            string += str(curr.value)
            string +=' -> '
            curr = curr.next
        string += 'None'
        return string


# list1 = LinkedList()
# list1.append(3)
# list1.append(14)
# list1.append(9)
# list1.append(9)
# list1.prepend(777)
# print(list1)
# list1.delete_value(9)
# list1.insert(2, 66)
# print(list1)
# list1.delete_tail()
# list1.delete_head()
# print(list1.is_value(10))
# print(list1)
# print(list1.get(1))
# print(len(list1))
# list1.delete(2)
# print(list1)
