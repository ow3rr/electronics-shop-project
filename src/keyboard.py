from src.item import Item


class MixinLang:
    """Для метода смены раскладки"""
    EN = "EN"

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        """Меняем расладку"""
        if self.__language.upper() == "EN":
            self.__language = "RU"
        elif self.__language.upper() == "RU":
            self.__language = "EN"
        return self

    @property
    def language(self):
        """Приват"""
        return self.__language


class Keyboard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
