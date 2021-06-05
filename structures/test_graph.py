"""This is a testing module"""

import itertools
from graph import Graph
import pytest


def form_parametrize_add_vertex():
    """Forming parameters for testing function add_vertex"""
    result, list_2, list_1 = [], [], Graph()

    for i in range(100):
        list_1.add_vertex(i)
        list_2.append(i)
        result.append((list_1.get_vertex(i), list_2[i]))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_add_vertex())


def test_add_vertex(test_arg, expected):
    """Testing function add_vertex"""
    assert test_arg == expected


def form_parametrize_add_edge():
    """Forming parameters for testing function add_edge"""
    result, vertex_1, vertex_2, list_2, list_1 = [], [], [], [], Graph()

    for i in range(50):
        vertex_1.append(i)
    for i in range(51, 100):
        vertex_2.append(i)

    vertex = [vertex_1, vertex_2]
    for elem in itertools.product(*vertex):
        list_1.add_edge(*elem)
        list_2.append(elem)

    for i in range(len(list_2)):
        result.append((list_1.get_edge(i), list_2[i]))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_add_edge())


def test_add_edge(test_arg, expected):
    """Testing function add_edge"""
    assert test_arg == expected


def form_parametrize_delete_edge():
    """Forming parameters for testing function delete_edge"""
    result, vertex_1, vertex_2, list_2, list_1 = [], [], [], [], Graph()

    for i in range(50):
        vertex_1.append(i)
    for i in range(51, 100):
        vertex_2.append(i)

    vertex = [vertex_1, vertex_2]

    for elem in itertools.product(*vertex):
        list_1.add_edge(*elem)
        list_2.append(elem)

    for _ in range(len(list_2) - 2):
        list_1.delete_edge(*list_1.get_edge(0))
        list_2 = list_2[1:]
        result.append((list_1.get_edge(0), list_2[0]))

    return result


@pytest.mark.parametrize("test_arg, expected",
                        form_parametrize_delete_edge())


def test_delete_edge(test_arg, expected):
    """Testing function delete_edge"""
    assert test_arg == expected
