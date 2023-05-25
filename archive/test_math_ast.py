from archive.math_ast import *


def test_number():
    exp = Expression.parse("3")
    assert exp.eval() == 3
    assert exp.infix() == "3"
    assert exp.infix_min() == "3"


def test_number2():
    exp = Expression.parse("-6")
    assert exp.eval() == -6
    assert exp.infix() == "-6"
    assert exp.infix_min() == "-6"


def test_add():
    exp = Expression.parse("3 4 +")
    assert exp.eval() == 3 + 4
    assert exp.infix() == "(3 + 4)"
    assert exp.infix_min() == "(3 + 4)"


def test_minus():
    exp = Expression.parse("3 4 -")
    assert exp.eval() == 3 - 4
    assert exp.infix() == "(3 - 4)"
    assert exp.infix_min() == "(3 - 4)"


def test_multiply():
    exp = Expression.parse("3 5 + 2 *")
    assert exp.eval() == ((3 + 5) * 2)
    assert exp.infix() == "((3 + 5) * 2)"
    assert exp.infix_min() == "((3 + 5) * 2)"


def test_divide():
    exp = Expression.parse("3 5 + 2 * 5 2 - /")
    assert exp.eval() == ((3 + 5) * 2) // (5 - 2)
    assert exp.infix() == "(((3 + 5) * 2) / (5 - 2))"
    assert exp.infix_min() == "(((3 + 5) * 2) / (5 - 2))"
