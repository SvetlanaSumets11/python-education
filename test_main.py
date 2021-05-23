"""This is a testing module"""

from to_test import even_odd, sum_all, Product, Shop
import pytest


@pytest.mark.parametrize("test_arg, expected",
                        [(3, "odd"),
                        (12, "even"),
                        (-244, "even"),
                        (11.0, "odd"),
                        (0, "even")])


def test_even_odd(test_arg, expected):
    """Function testing even_odd when parameters are passed"""
    assert even_odd(test_arg) == expected


def test_even_odd_none_arg():
    """Function testing even_odd when passed None"""
    with pytest.raises(TypeError):
        even_odd(None)


def test_even_odd_str():
    """Function testing even_odd when the wrong type is passed"""
    with pytest.raises(TypeError):
        sum_all("greetings")


@pytest.mark.parametrize("test_arg, expected",
                        [([2, 1], 3),
                        ([3.4, 5.6, 7.8], 16.8),
                        ([0, 0.7, -23], -22.3),
                        ([], 0)])


def test_func_sum(test_arg, expected):
    """Function testing sum_all when parameters are passed"""
    assert sum_all(*test_arg) == expected


def test_sum_none_arg():
    """Function testing sum_all when passed None"""
    with pytest.raises(TypeError):
        sum_all(None)


def test_sum_str():
    """Function testing sum_all when the wrong type is passed"""
    letters = list("greetings")
    with pytest.raises(TypeError):
        sum_all(letters)


@pytest.fixture()
def product():
    """Fixture - creates an instance of the class Product"""
    return Product("apple", 15.2, 20)


@pytest.mark.parametrize("test_arg, expected",
                        [(3, 17),
                        (20, 0),
                        (0, 20)])


def test_product_subtract_quantity(product, test_arg, expected):
    """Function testing subtract_quantity when parameters are passed"""
    product.subtract_quantity(test_arg)
    assert product.quantity == expected


def test_product_subtract_quantity_none_arg(product):
    """Function testing subtract_quantity when passed None"""
    with pytest.raises(TypeError):
        product.subtract_quantity(None)


def test_product_subtract_quantity_str(product):
    """Function testing subtract_quantity when the wrong type is passed"""
    with pytest.raises(TypeError):
        product.subtract_quantity("greetings")


@pytest.mark.parametrize("test_arg, expected",
                        [(3, 23),
                        (0, 20)])


def test_product_add_quantity(product, test_arg, expected):
    """Function testing add_quantity when parameters are passed"""
    product.add_quantity(test_arg)
    assert product.quantity == expected


def test_product_add_quantity_none_arg(product):
    """Function testing add_quantity when passed None"""
    with pytest.raises(TypeError):
        product.add_quantity(None)


def test_product_add_quantity_str(product):
    """Function testing add_quantity when the wrong type is passed"""
    with pytest.raises(TypeError):
        product.add_quantity("greetings")


@pytest.mark.parametrize("test_arg, expected",
                        [(11.5, 11.5),
                        (25.0, 25.0)])


def test_product_change_price(product, test_arg, expected):
    """Function testing change_price when parameters are passed"""
    product.change_price(test_arg)
    assert product.price == expected


@pytest.fixture()
def shop():
    """Fixture - creates an instance of the class Shop"""
    return Shop([Product("banana", 13.3, 10), Product("apple", 15.2, 20)])


def test_shop_add_product(shop):
    """Function testing add_product when parameters are passed"""
    shop.add_product(product)
    assert len(shop.products) == 3


@pytest.mark.parametrize("test_arg, expected",
                        [("banana", 0),
                        ("apple", 1),
                        ("potato", None)])


def test_shop_get_product_index(shop, test_arg, expected):
    """Function testing _get_product_index when parameters are passed"""
    assert shop._get_product_index(test_arg) == expected


@pytest.mark.parametrize("test_arg, expected",
                        [(["banana", 10], 133),
                        (["apple", 10], 152)])


def test_shop_sell_product(shop, test_arg, expected):
    """Function testing sell_product when parameters are passed. Function result"""
    assert shop.sell_product(*test_arg) == expected


@pytest.mark.parametrize("test_arg",
                        [(["banana", 30]),
                        (["apple", 30])])


def test_shop_sell_product_not_enough_products(shop, test_arg):
    """Function testing sell_product when not enough products"""
    with pytest.raises(ValueError):
        shop.sell_product(*test_arg)


@pytest.mark.parametrize("test_arg, expected",
                        [(["banana", 10], 1),
                        (["apple", 20], 1)])


def test_shop_sell_product_del_products(shop, test_arg, expected):
    """Function testing sell_product when del products"""
    shop.sell_product(*test_arg)
    assert len(shop.products) == expected


@pytest.mark.parametrize("test_arg, expected",
                        [(["banana", 9], 1),
                        (["apple", 10], 10)])


def test_shop_sell_product_quantity(shop, test_arg, expected):
    """Function testing sell_product when subtract quantity products"""
    product, _ = test_arg
    product_index = shop._get_product_index(product)
    shop.sell_product(*test_arg)
    assert shop.products[product_index].quantity == expected


@pytest.mark.parametrize("test_arg, expected",
                        [(["banana", 10], 133),
                        (["apple", 10], 152)])


def test_shop_sell_product_money(shop, test_arg, expected):
    """Function testing sell_product when parameters are passed. Value money"""
    shop.sell_product(*test_arg)
    assert shop.money == expected
