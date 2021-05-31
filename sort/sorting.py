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


def partition(mass, left, right):
    """partition function for the iterative quick sort method"""
    ind = left - 1
    elem = mass[right]

    for item in range(left, right):
        if mass[item] <= elem:
            ind += 1
            mass[ind], mass[item] = mass[item], mass[ind]

    mass[ind + 1], mass[right] = mass[right], mass[ind + 1]
    return ind + 1


def iter_quick_sort(mass):
    """A function that implements the iterative quick sort method for the list"""
    left, right = 0, len(mass) - 1
    memory = [0] * (right + left + 1)
    memory[0], memory[1], top = left, right, 1

    while top >= 0:
        right = memory[top]
        top -= 1
        left = memory[top]
        top -= 1
        elem = partition(mass, left, right)

        if elem - 1 > left:
            top += 1
            memory[top] = left
            top += 1
            memory[top] = elem - 1

        if elem + 1 < right:
            top += 1
            memory[top] = elem + 1
            top += 1
            memory[top] = right
