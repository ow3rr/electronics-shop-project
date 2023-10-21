import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, meter):
        if len(meter) < 10:
            self._name = meter
        else:
            self._name = meter[:10]

    """атрибут `name` сделать приватным
    добавить геттер и сеттер для `name`, используя @property
    в сеттере `name` проверять, что длина наименования товара не больше 10 симвовов,
    в противном случае, обрезать строку (оставить первые 10 символов)."""

    @classmethod
    def instantiate_from_csv(cls, filename):
        cls.all = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                item = cls(i["name"], i["price"], i["quantity"])
                cls.all.append(item)
            return cls.all
    """`instantiate_from_csv()` - класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
"""

    @staticmethod
    def string_to_number(str_num):
        return int(float(str_num))
    """`string_to_number()` - статический метод, возвращающий число из числа-строки"""

    def calculate_total_price(self) -> float:
        total_price = self.price * self.quantity
        return total_price

    """
    Рассчитывает общую стоимость конкретного товара в магазине.

    :return: Общая стоимость товара.
    """

    def apply_discount(self) -> None:
        self.price *= self.pay_rate
        return self.price

    """
    Применяет установленную скидку для конкретного товара.
    """
