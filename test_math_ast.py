from math_ast import *


def test_number():
    exp = ExpressionParser.parse("3")
    assert exp.eval() == 3
    assert exp.infix() == "3"
    assert exp.infix_min() == "3"


def test_number2():
    exp = ExpressionParser.parse("-6")
    assert exp.eval() == -6
    assert exp.infix() == "-6"
    assert exp.infix_min() == "-6"


def test_add():
    exp = ExpressionParser.parse("3 4 +")
    assert exp.eval() == 3 + 4
    assert exp.infix() == "(3 + 4)"
    assert exp.infix_min() == "(3 + 4)"


def test_minus():
    exp = ExpressionParser.parse("3 4 -")
    assert exp.eval() == 3 - 4
    assert exp.infix() == "(3 - 4)"
    assert exp.infix_min() == "(3 - 4)"


def test_multiply():
    exp = ExpressionParser.parse("3 5 + 2 *")
    assert exp.eval() == ((3 + 5) * 2)
    assert exp.infix() == "((3 + 5) * 2)"
    assert exp.infix_min() == "((3 + 5) * 2)"


def test_divide():
    exp = ExpressionParser.parse("3 5 + 2 * 5 2 - /")
    assert exp.eval() == ((3 + 5) * 2) // (5 - 2)
    assert exp.infix() == "(((3 + 5) * 2) / (5 - 2))"
    assert exp.infix_min() == "(((3 + 5) * 2) / (5 - 2))"
