"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.keyboard import Keyboard

@pytest.fixture
def test_pay_rate():
    assert 0 < Item.pay_rate <= 1


def test_quantity():
    item1 = Item("Ноутбук", 20000, 5)
    assert item1.price > 0
    assert item1.quantity > 0


def test_calculate_total_price():
    assert Item("Ноутбук", 20000, 5).calculate_total_price() > 0


def test_class_item():
    return Item('Ноутбук', 10, 5)


def test_string_to_number():
    number = Item.string_to_number('123')
    assert number == 123


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_class_phone():
    assert Phone("iPhone 14", 120_000, 5, 2)


def test_str_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_repr_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_sim_above_zero():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_add_quantity_on_item():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25


def test_add_quantity_on_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert phone1 + item1 == 25


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_lang(keyboard):
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"
    assert kb.language != 'CH'


def test_exception_instantiate_from_csv():
    with pytest.raises(FileNotFoundError) as e:
        Item.instantiate_from_csv('sssss')
    assert str(e.value) == "Отсутствует файл item.csv"

    with pytest.raises(InstantiateCSVError) as e:
        Item.instantiate_from_csv('tests/test_items.csv')
    assert str(e.value) == 'Файл item.csv поврежден'