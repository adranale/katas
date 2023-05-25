import string
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Expression(ABC):
    @abstractmethod
    def eval(self) -> int:
        pass

    @abstractmethod
    def infix(self) -> str:
        pass

    def infix_min(self) -> str:
        return self.infix()

    @classmethod
    def parse(cls, exp_str: str):
        exp_list = exp_str.split()
        result, rest = cls.parse_list(exp_list)
        assert not rest
        return result

    @classmethod
    def parse_list(cls, exp_list: list[str]):
        if 1 <= len(exp_list):
            exp = exp_list[-1]
            try:  # number
                return Number.parse(exp), exp_list[:-1]
            except ValueError:  # not number, operation
                op = exp
                right, rest = Expression.parse_list(exp_list[:-1])
                left, rest = Expression.parse_list(rest)
                return Operation.create(op=op, left=left, right=right), rest


@dataclass
class Number(Expression):
    value: int

    @classmethod
    def parse(cls, exp_str: str):
        return Number(int(exp_str))

    def eval(self) -> int:
        return self.value

    def infix(self) -> str:
        return str(self.value)


@dataclass
class Operation(Expression):
    op: str
    right: Expression
    left: Expression

    def eval(self) -> Optional[int]:
        match self.op:
            case "+":
                return self.left.eval() + self.right.eval()
            case "-":
                return self.left.eval() - self.right.eval()
            case "*":
                return self.left.eval() * self.right.eval()
            case "/":
                return self.left.eval() // self.right.eval()
            case _:
                return None

    def infix(self) -> str:
        return f"({self.left.infix()} {self.op} {self.right.infix()})"

    @classmethod
    def create(cls, op: str, left: Expression, right: Expression) -> Expression:
        return Operation(op=op, left=left, right=right)

