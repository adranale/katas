import pytest as pytest

from cupcake import *


def test_cupcake():
    c = Cupcake()
    assert "Cupcake" == c.get_name()
    assert 1.0 == c.get_price()


def test_cookie():
    c = Cookie()
    assert "Cookie" == c.get_name()
    assert 2.0 == c.get_price()


def test_sugar_cookie():
    c = Sugar(Cookie())
    assert "Cookie with Sugar" == c.get_name()
    assert 2.1 == c.get_price()


def test_sugar_cupcake():
    c = Sugar(Cupcake())
    assert "Cupcake with Sugar" == c.get_name()
    assert 1.1 == c.get_price()


def test_choc_cupcake():
    c = Chocolate(Cupcake())
    assert "Cupcake with Chocolate" == c.get_name()
    assert 1.1 == c.get_price()


def test_nuts_cupcake():
    c = Nuts(Cupcake())
    assert "Cupcake with Nuts" == c.get_name()
    assert 1.2 == c.get_price()


def test_sugar_nuts_cookie():
    c = Sugar(Nuts(Cupcake()))
    assert "Cupcake with Nuts and Sugar" == c.get_name()
    assert 1.3 == c.get_price()


def test_bundle():
    bundle = [Cupcake(), Cookie(), Sugar(Cookie()), Sugar(Cupcake()), Chocolate(Cupcake()), Nuts(Cupcake()),
              Sugar(Nuts(Cookie()))]
    bundle = Bundle(bundle)
    name = bundle.get_name()
    assert "Bundle of: Cupcake, Cookie, Cookie with Sugar, Cupcake with Sugar, Cupcake with Chocolate, Cupcake with Nuts, Cookie with Nuts and Sugar" == name
    price = bundle.get_price()
    # assert 9.72 == price
    assert abs(9.72 - price) <= 0.01
    pytest.approx(9.72, price, 0.01)
