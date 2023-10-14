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
