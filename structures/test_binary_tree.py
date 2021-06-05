"""This is a testing module"""

from random import randint
from binary_tree import BinaryTree
import pytest


def form_parametrize_add():
    """Forming parameters for testing function add"""
    result, list_1 = [], BinaryTree(100)

    for _ in range(100):
        value = randint(0, 1000)
        list_1.add(value)
        result.append((list_1.find(value), True))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_add())


def test_add(test_arg, expected):
    """Testing function add"""
    assert test_arg == expected


def form_parametrize_delete():
    """Forming parameters for testing function delete"""
    result, list_1 = [], BinaryTree(100)

    for _ in range(100):
        value = randint(0, 1000)
        list_1.add(value)
        list_1.delete(value)
        result.append((list_1.find(value), False))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_delete())


def test_delete(test_arg, expected):
    """Testing function delete"""
    assert test_arg == expected
