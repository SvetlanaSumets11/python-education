"""This module to implement a hash table"""

from linked_list import LinkedList

class LinkedListHash(LinkedList):
    """This is the linked list class for the hash table"""

    def is_value(self, key):
        """Method for checking the existence of a node with a given value in the list"""
        current = self.head
        while current is not None:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None


class HashTable:
    """This is the hash table class"""
    def __init__(self, size):
        self.size = size
        self.table = [LinkedListHash() for _ in range(size)]

    def hash_code(self, string):
        """Method for calculating the hash code"""
        return sum(ord(item) for item in string) % self.size

    def __getitem__(self, string):
        return self.table[self.hash_code(string)].is_value(string)

    def __setitem__(self, string, value):
        if self[string] is None:
            self.table[self.hash_code(string)].append((string, value))

    def print_table(self):
        """Hash table output"""
        for item in self.table:
            print(str(item))


# has = HashTable(20)
# has["Hello"] = 5
# has["eHllo"] = 5
# has["My_world"] = 1
# print(has.hash_code("Hello"))
# has.print_table()
