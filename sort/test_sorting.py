"""This is a testing module"""

from math import factorial
from random import randint, choice
from sorting import fact, binary_search, quick_sort
import pytest


random_mass = lambda val_1, val_2, size: [randint(val_1, val_2) for _ in range(size)]


def form_parametrize_quick_sort():
    """Forming parameters for testing quick sort"""
    result = []
    for _ in range(1000):
        mass = random_mass(1, 1000, 1000)
        result.append((mass, sorted(mass)))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_quick_sort())


def test_quick_sort(test_arg, expected):
    """Testing Quick Sort"""
    assert quick_sort(test_arg) == expected


def form_parametrize_binary_search_true():
    """We form parameters for testing binary search in the case when
    the element is contained in the list"""
    result = []
    for _ in range(1000):
        mass = [i for i in range(1000)]
        value = choice(mass)
        result.append(((mass, value), True))
    return result


def form_parametrize_binary_search_false():
    """We form parameters for testing binary search in the case when
    the element is not contained in the list"""
    result = []
    for _ in range(1000):
        mass = [i for i in range(1000)]
        value = randint(0, 1000)
        while value in mass:
            value = randint(0, 1000)
        result.append(((mass, value), False))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_binary_search_true())


def test_binary_search_true(test_arg, expected):
    """Testing binary search"""
    assert binary_search(*test_arg) == expected


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_binary_search_false())


def test_binary_search_false(test_arg, expected):
    """Testing binary search"""
    assert binary_search(*test_arg) == expected


def form_parametrize_factorial():
    """Forming parameters for testing the factorial"""
    result = []
    for _ in range(1000):
        value = randint(0, 900)
        result.append((value, factorial(value)))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_factorial())


def test_factorial(test_arg, expected):
    """Testing the factorial"""
    assert fact(test_arg) == expected
