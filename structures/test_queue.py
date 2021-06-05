"""This is a testing module"""

from random import randint
from queue import Queue
import pytest


def form_parametrize_enqueue():
    """Forming parameters for testing function enqueue"""
    result, list_2, list_1 = [], [], Queue()

    for i in range(100):
        value = randint(0, 1000)
        list_1.enqueue(value)
        list_2.append(value)
        result.append((list_1.peek_tail(), list_2[i]))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_enqueue())


def test_enqueue(test_arg, expected):
    """Testing function enqueue"""
    assert test_arg == expected


def form_parametrize_dequeue():
    """Forming parameters for testing function dequeue"""
    result, list_2, list_1 = [], [], Queue()

    for _ in range(101):
        value = randint(0, 1000)
        list_1.enqueue(value)
        list_2.append(value)

    for _ in range(100):
        list_1.dequeue()
        list_2 = list_2[1:]
        result.append((list_1.peek_head(), list_2[0]))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_dequeue())


def test_dequeue(test_arg, expected):
    """Testing function dequeue"""
    assert test_arg == expected
