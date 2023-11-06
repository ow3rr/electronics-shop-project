import csv
import os


class InstantiateCSVError(Exception):
    pass

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        """- атрибут `name` сделать приватным"""
        return self._name

    @name.setter
    def name(self, meter):
        """- добавить геттер и сеттер для `name`, используя @property
        - в сеттере `name` проверять, что длина наименования товара не больше 10 симвовов. В противном случае, обрезать строку (оставить первые 10 символов).
        """
        if len(meter) < 10:
            self._name = meter
        else:
            self._name = meter[:10]

    @classmethod
    def instantiate_from_csv(cls, filename='src/items.csv'):
        """`instantiate_from_csv()` - класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
    """
        try:
            with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), filename)) as file:
                reader = csv.DictReader(file)
                cls.all.clear()
                for i in reader:
                    cls(i['name'], float(i['price']), int(i['quantity']))

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except Exception:
            raise InstantiateCSVError("Файл item.csv поврежден")
    @staticmethod
    def string_to_number(str_num):
        """`string_to_number()` - статический метод, возвращающий число из числа-строки"""
        return int(float(str_num))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity