import string
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Expression(ABC):

    def infix(self) -> str:
        return ExpressionInfixPrinter().visit_expression(self)

    def eval(self) -> int:
        return ExpressionEvaluator().visit_expression(self)

    def infix_min(self) -> str:
        return ExpressionInfixMinimalPrinter().visit_expression(self)


@dataclass
class Number(Expression):
    value: int


@dataclass
class Operation(Expression):
    op: str
    right: Expression
    left: Expression


class ExpressionParser:

    @classmethod
    def parse(cls, exp_str: str):
        exp_list = exp_str.split()
        result, rest = cls.parse_list(exp_list)
        assert not rest
        return result

    @classmethod
    def parse_list(cls, exp_list: list[str]) -> (Expression, list[str]):
        if 1 <= len(exp_list):
            exp = exp_list[-1]
            try:  # number
                return cls.parse_number(exp), exp_list[:-1]
            except ValueError:  # not number, operation
                op = exp
                right, rest = cls.parse_list(exp_list[:-1])
                left, rest = cls.parse_list(rest)
                return cls.create_op(op=op, left=left, right=right), rest

    @classmethod
    def parse_number(cls, exp_str: str) -> Number:
        return Number(int(exp_str))

    @classmethod
    def create_op(cls, op: str, left: Expression, right: Expression) -> Operation:
        return Operation(op=op, left=left, right=right)


class ExpressionVisitor(ABC):

    @abstractmethod
    def visit_expression(self, exp: Expression):
        pass

    @abstractmethod
    def _visit_number(self, number: Number):
        pass

    @abstractmethod
    def _visit_operation(self, op: Operation):
        pass


class ExpressionEvaluator(ExpressionVisitor):

    def visit_expression(self, exp: Expression):
        if isinstance(exp, Number):
            return self._visit_number(exp)
        elif isinstance(exp, Operation):
            return self._visit_operation(exp)

    def _visit_number(self, number: Number):
        return number.value

    def _visit_operation(self, op: Operation):
        match op.op:
            case "+":
                return self.visit_expression(op.left) + self.visit_expression(op.right)
            case "-":
                return self.visit_expression(op.left) - self.visit_expression(op.right)
            case "*":
                return self.visit_expression(op.left) * self.visit_expression(op.right)
            case "/":
                return self.visit_expression(op.left) // self.visit_expression(op.right)
            case _:
                return None


class ExpressionInfixPrinter(ExpressionVisitor):

    def visit_expression(self, exp: Expression):
        if isinstance(exp, Number):
            return self._visit_number(exp)
        elif isinstance(exp, Operation):
            return self._visit_operation(exp)

    def _visit_number(self, number: Number):
        return str(number.value)

    def _visit_operation(self, op: Operation):
        return f"({self.visit_expression(op.left)} {op.op} {self.visit_expression(op.right)})"


class ExpressionInfixMinimalPrinter(ExpressionVisitor):

    def visit_expression(self, exp: Expression):
        print_string = ExpressionInfixPrinter().visit_expression(exp)

        return print_string

    def _visit_number(self, number: Number):
        pass

    def _visit_operation(self, op: Operation):
        pass
