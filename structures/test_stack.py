"""This is a testing module"""

from random import randint
from stack import Stack
import pytest


def form_parametrize_push():
    """Forming parameters for testing function push"""
    result, list_2, list_1 = [], [], Stack()

    for i in range(100):
        value = randint(0, 1000)
        list_1.push(value)
        list_2.append(value)
        result.append((list_1.peek(), list_2[i]))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_push())


def test_push(test_arg, expected):
    """Testing function push"""
    assert test_arg == expected


def form_parametrize_pop():
    """Forming parameters for testing function pop"""
    result, list_2, list_1 = [], [], Stack()

    for _ in range(101):
        value = randint(0, 1000)
        list_1.push(value)
        list_2.append(value)

    for _ in range(100):
        list_1.pop()
        list_2 = list_2[:-1]

        result.append((list_1.peek(), list_2[-1]))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_pop())


def test_pop(test_arg, expected):
    """Testing function pop"""
    assert test_arg == expected
