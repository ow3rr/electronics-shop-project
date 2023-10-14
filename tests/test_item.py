"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_pay_rate():
    assert 0 < Item.pay_rate <= 1


def test_quantity():
    item1 = Item("Ноутбук", 20000, 5)
    assert item1.price > 0
    assert item1.quantity > 0


def test_calculate_total_price():
    assert Item("Ноутбук", 20000, 5).calculate_total_price() > 0

