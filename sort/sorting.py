"""This module to implement binary search, quicksort and recursive factorial"""

from random import choice

def fact(value):
    """Function that implements finding the factorial of a number"""
    if value == 0:
        return 1
    return fact(value - 1) * value


def binary_search(mass, value):
    """A function that implements binary search in a sorted list"""
    if len(mass) == 0:
        return False

    index_middle = len(mass)//2

    if value == mass[index_middle]:
        return True
    if value < mass[index_middle]:
        return binary_search(mass[:index_middle], value)
    if value > mass[index_middle]:
        return binary_search(mass[index_middle + 1:], value)


def quick_sort(mass):
    """A function that implements the quick sort method for the list"""
    if len(mass) <= 1:
        return mass

    pivot = choice(mass)
    less, more, equal = [], [], []

    for item in mass:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        elif item == pivot:
            equal.append(item)

    return quick_sort(less) + equal + quick_sort(more)
