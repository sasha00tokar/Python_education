from example.Shop import Bag, Item
import pytest


def test_sum_price():
    basket = Bag()
    product_1 = Item('banana', 4)
    basket.add_bag(product_1)
    basket.bulk_discount_price()
    assert basket.sum_price() == 31


def test_del_from_bag():
    basket = Bag()
    product_1 = Item('banana', 3)
    product_2 = Item('banana', 1)
    basket.add_bag(product_1)
    assert basket.del_from_bag(product_2) is True


def test_add_bag():
    basket = Bag()
    product_1 = Item('banana', 3)
    basket.add_bag(product_1)
    assert  basket.shopping_list['banana']['count'] == 3


def test_show_bag():
    basket = Bag()
    product = Item('apple', 1)
    basket.add_bag(product)
    assert basket.show_bag() == {'apple': {'count': 1, 'price': 20}}


def test_bulk_discount_price():
    basket = Bag()
    produkt = Item('apple', 1)
    basket.add_bag(produkt)
    basket.bulk_discount_price()
    assert basket.shopping_list['apple']['price'] == 20