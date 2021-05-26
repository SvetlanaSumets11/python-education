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
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.find(value)
        else:
            return True

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
