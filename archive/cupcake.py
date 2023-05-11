from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass


class Cupcake(Food):
    def get_name(self) -> str:
        return "Cupcake"

    def get_price(self) -> float:
        return 1.0


class Cookie(Food):
    def __init__(self, basic: Food = None) -> None:
        self._basic = basic

    def get_name(self) -> str:
        return "Cookie"

    def get_price(self) -> float:
        return 2.0


class Chocolate(Food):
    def __init__(self, basic: Food) -> None:
        self._basic = basic

    def get_name(self) -> str:
        if type(self._basic) is Cupcake or type(self._basic) is Cookie:
            return self._basic.get_name() + " with Chocolate"
        else:
            return self._basic.get_name() + " and Chocolate"

    def get_price(self) -> float:
        return self._basic.get_price() + 0.1


class Nuts(Food):
    def __init__(self, basic: Food) -> None:
        self._basic = basic

    def get_name(self) -> str:
        if type(self._basic) is Cupcake or type(self._basic) is Cookie:
            return self._basic.get_name() + " with Nuts"
        else:
            return self._basic.get_name() + " and Nuts"

    def get_price(self) -> float:
        return self._basic.get_price() + 0.2


class Sugar(Food):
    def __init__(self, basic: Food) -> None:
        self._basic = basic

    def get_name(self) -> str:
        if type(self._basic) is Cupcake or type(self._basic) is Cookie:
            return self._basic.get_name() + " with Sugar"
        else:
            return self._basic.get_name() + " and Sugar"

    def get_price(self) -> float:
        return self._basic.get_price() + 0.1


if __name__ == '__main__':
    food = Sugar(Cupcake())
    food = Chocolate(food)
    print(food.get_name() + ": " + str(food.get_price()))

    food = Cookie()
    food = Nuts(food)
    print(food.get_name() + ": " + str(food.get_price()))