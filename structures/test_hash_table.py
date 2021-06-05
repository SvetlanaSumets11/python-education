"""This is a testing module"""

from hash_table import HashTable
import pytest


def form_parametrize_add():
    """Forming parameters for testing function add"""
    dict_1 = {item: item ** 2 for item in range(100)}
    dict_2 = HashTable(100)
    result = []

    for i in range(100):
        dict_2.add(str(i), i ** 2)
        result.append((dict_2[str(i)], dict_1.get(i)))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_add())


def test_append(test_arg, expected):
    """Testing function add"""
    assert test_arg == expected



def form_parametrize_delete():
    """Forming parameters for testing function delete"""
    dict_1 = {item: item ** 2 for item in range(100)}
    dict_2 = HashTable(100)
    result = []

    for i in range(100):
        dict_1.pop(i)
        dict_2.delete(str(i))
        result.append((dict_2.find(str(i)), bool(dict_1.get(i))))
    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_delete())


def test_delete(test_arg, expected):
    """Testing function delete"""
    assert test_arg == expected
