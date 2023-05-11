from abc import ABC, abstractmethod
from typing import List


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

    def get_name(self) -> str:
        return "Cookie"

    def get_price(self) -> float:
        return 2.0


class Topping(Food):
    def __init__(self, basic: Food) -> None:
        self._basic = basic

    def get_name(self) -> str:
        if type(self._basic) is Cupcake or type(self._basic) is Cookie:
            return self._basic.get_name() + " with " + self._get_topping_name()
        else:
            return self._basic.get_name() + " and " + self._get_topping_name()

    def get_price(self) -> float:
        return self._basic.get_price() + self._get_topping_price()

    @abstractmethod
    def _get_topping_name(self) -> str:
        pass

    @abstractmethod
    def _get_topping_price(self) -> float:
        pass


class Chocolate(Topping):
    def __init__(self, basic: Food) -> None:
        super().__init__(basic)

    def _get_topping_name(self) -> str:
        return "Chocolate"

    def _get_topping_price(self) -> float:
        return 0.1


class Nuts(Topping):
    def __init__(self, basic: Food) -> None:
        super().__init__(basic)

    def _get_topping_name(self) -> str:
        return "Nuts"

    def _get_topping_price(self) -> float:
        return 0.2


class Sugar(Topping):
    def __init__(self, basic: Food) -> None:
        super().__init__(basic)

    def _get_topping_name(self) -> str:
        return "Sugar"

    def _get_topping_price(self) -> float:
        return 0.1


class Bundle(Food):
    cakes: List[Food] = []
    def __init__(self, cakes: List[Food]) -> None:
        self.cakes = cakes

    def get_name(self) -> str:
        name = "Bundle of: "
        for cake in self.cakes:
            name += cake.get_name() + ", "
        return name[:-2]

    def get_price(self) -> float:
        total = 0.0
        for cake in self.cakes:
            total += cake.get_price()
        return total * 0.9


if __name__ == '__main__':
    food1 = Cupcake()
    print(food1.get_name() + ": " + str(food1.get_price()))

    food2 = Cookie()
    print(food2.get_name() + ": " + str(food2.get_price()))

    food3 = Cupcake()
    food3 = Chocolate(food3)
    print(food3.get_name() + ": " + str(food3.get_price()))

    food4 = Cookie()
    food4 = Nuts(food4)
    print(food4.get_name() + ": " + str(food4.get_price()))

    food5 = Cookie()
    food5 = Chocolate(food5)
    print(food5.get_name() + ": " + str(food5.get_price()))

    food6 = Sugar(Cupcake())
    food6 = Chocolate(food6)
    print(food6.get_name() + ": " + str(food6.get_price()))

    food7 = Sugar(Cookie())
    food7 = Chocolate(food7)
    print(food7.get_name() + ": " + str(food7.get_price()))

    food8 = Cookie()
    food8 = Nuts(food8)
    print(food8.get_name() + ": " + str(food8.get_price()))

    food9 = Cookie()
    food9 = Chocolate(food9)
    print(food9.get_name() + ": " + str(food9.get_price()))

    bundle = [food1, food2, food3, food4, food5, food6, food7, food8, food9]
    bundle_object = Bundle()
    bundle_object.cakes = bundle
    print(str(bundle_object.get_name() + ": " + str(bundle_object.get_price())))
