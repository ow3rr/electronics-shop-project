from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, (Phone, Item)):
            raise ValueError("Нельзя сложить Item с экземпляром не Phone или Item класса.")
        return self.quantity + other.quantity

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_card):
        if sim_card > 0:
            self.__number_of_sim = sim_card
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
