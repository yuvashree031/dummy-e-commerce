from utils import calculate_tax


def test_tax_100():
    assert calculate_tax(100) == 18


def test_tax_1000():
    assert calculate_tax(1000) == 180


def test_tax_zero():
    assert calculate_tax(0) == 0