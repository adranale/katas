from dataclasses import dataclass
from typing import List
from enum import Enum


class Topping(Enum):
    COOKIE = 2.0
    CHOCOLATE = 0.1
    NUTS = 0.1
    SUGAR = 0.1


@dataclass
class Cupcake:
    toppings: List[Topping]

    def get_name(self) -> str:
        full_name = "Cupcake with"
        for topping in self.toppings:
            full_name += " " + topping.name
        return full_name

    def get_price(self) -> float:
        total = 1.0
        for topping in self.toppings:
            total += topping.value
        return total


