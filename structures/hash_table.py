"""This module to implement a hash table"""

from linked_list import LinkedList

class LinkedListHash(LinkedList):
    """This is the linked list class for the hash table"""

    def this_value(self, key):
        """Method for checking the existence of a node with a given value in the list"""
        current = self.head
        while current is not None:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def delete_value(self, key):
        """Method for removing a node / nodes by a given key from the list"""
        if self.is_empty():
            print("Список пуст")
        else:
            current = self.head
            ind = 0

            while current is not None:
                if current.value[0] == key:
                    self.delete(ind)
                else:
                    ind += 1
                current = current.next


class HashTable:
    """This is the hash table class"""
    def __init__(self, size):
        self.size = size
        self.table = [LinkedListHash() for _ in range(size)]

    def hash_code(self, string):
        """Method for calculating the hash code"""
        return sum(ord(item) for item in string) % self.size

    def __getitem__(self, string):
        return self.table[self.hash_code(string)].this_value(string)

    def __setitem__(self, string, value):
        if self[string] is None:
            self.table[self.hash_code(string)].append((string, value))

    def print_table(self):
        """Hash table output"""
        for item in self.table:
            print(str(item))

    def delete(self, string):
        """Delete node by key"""
        if self[string] is not None:
            self.table[self.hash_code(string)].delete_value(string)

    def find(self, string):
        """Find node by key"""
        return self[string] is not None

    def add(self, string, value):
        """Add node"""
        self[string] = value


# has = HashTable(20)
# has["Hello"] = 5
# has["eHllo"] = 5
# has["My_world"] = 1
# has["My love"] = 9
# print(has.hash_code("Hello"))
# has.print_table()
# print(has["eHllo"])
# print(has.find("eHllo"))
# has.delete("eHllo")
# print()
# has.print_table()
# print(has.find("eHllo"))
# print(has["eHllo"])
