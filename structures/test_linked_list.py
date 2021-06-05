"""This is a testing module"""

from random import randint
from linked_list import LinkedList
import pytest


def form_parametrize_append():
    """Forming parameters for testing function append"""
    result, list_2, list_1 = [], [], LinkedList()

    for i in range(100):
        value = randint(0, 1000)
        list_1.append(value)
        list_2.append(value)
        result.append((list_1.get(i), list_2[i]))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_append())


def test_append(test_arg, expected):
    """Testing function append"""
    assert test_arg == expected


def form_parametrize_prepend():
    """Forming parameters for testing function prepend"""
    result, list_2, list_1 = [], [], LinkedList()

    for i in range(100):
        value = randint(0, 1000)
        list_1.prepend(value)
        list_2.insert(0, value)
        result.append((list_1.get(i), list_2[i]))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_prepend())


def test_prepend(test_arg, expected):
    """Testing function prepend"""
    assert test_arg == expected


def form_parametrize_insert():
    """Forming parameters for testing function insert"""
    result, list_2, list_1 = [], [], LinkedList()

    for i in range(100):
        value = randint(0, 1000)
        list_1.insert(i, value)
        list_2.insert(i, value)
        result.append((list_1.get(i), list_2[i]))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_insert())


def test_insert(test_arg, expected):
    """Testing function insert"""
    assert test_arg == expected


def form_parametrize_delete():
    """Forming parameters for testing function delete"""
    result, list_2, list_1 = [], [], LinkedList()

    for _ in range(100):
        value = randint(0, 1000)
        list_1.append(value)
        list_2.append(value)

    for _ in range(100):
        list_1.delete(0)
        list_2 = list_2[1:]

        mass = []
        for j in range(len(list_1)):
            mass.append(list_1.get(j))

        result.append((mass, list_2))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_delete())


def test_delete(test_arg, expected):
    """Testing function delete"""
    assert test_arg == expected


def form_parametrize_delete_value():
    """Forming parameters for testing function delete_value"""
    result, list_2, list_1 = [], [], LinkedList()

    for _ in range(100):
        value = randint(0, 1000)
        list_1.append(value)
        list_2.append(value)

    for _ in range(100):
        list_1.delete(list_1[0])
        list_2.remove(list_2[0])

        mass = []
        for j in range(len(list_1)):
            mass.append(list_1.get(j))

        result.append((mass, list_2))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_delete())


def test_delete_value(test_arg, expected):
    """Testing function delete_value"""
    assert test_arg == expected
