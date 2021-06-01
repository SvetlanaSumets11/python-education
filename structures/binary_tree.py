"""This module is for implementing a binary tree"""

class BinaryTree:
    """This binary tree class"""
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add(self, value):
        """Adding a node to a tree"""
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.add(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.add(value)

    def find(self, value):
        """Method for finding a node in a tree"""
        if value < self.value:
            if self.left is None:
                return False
            return self.left.find(value)
        if value > self.value:
            if self.right is None:
                return False
            return self.right.find(value)
        if value == self.value:
            return True

    def find_min(self, node):
        """helper function to remove a node from a tree"""
        return self.find_min(node.left) if node.left is not None else node

    def delete(self, value, node = None):
        """function to remove a node from a tree"""
        if not self.find(value):
            raise ValueError("Нет узла с таким значением")
        if node is None:
            node = self
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete(value, node.left)
            return node
        if value > node.value:
            node.right = self.delete(value, node.right)
            return node

        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        if node.left is not None and node.right is not None:
            min_value = self.find_min(node.right).value
            node.value = min_value
            node.right = self.delete(min_value, node.right)
            return node

    def __str__(self, level=0, unit=''):
        res = ""
        if self.left:
            res += self.left.__str__(level + 1, '/')
        res += '\t' * level + f'{unit} {self.value}\n'
        if self.right:
            res += self.right.__str__(level + 1, '\\')
        return res

# tree = BinaryTree(27)
# tree.add(14)
# tree.add(35)
# tree.add(31)
# tree.add(10)
# tree.add(19)
# print(tree.find(20))
# print(tree)
# print(tree.find(7))
# print(tree.find(14))
# tree.delete(35)
# print(tree)
