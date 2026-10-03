from even_odd_checker import check_even_odd


def test_even_number():
    assert check_even_odd(10) == "Even"


def test_odd_number():
    assert check_even_odd(7) == "Odd"


def test_zero():
    assert check_even_odd(0) == "Even"


def test_negative_even_number():
    assert check_even_odd(-8) == "Even"


def test_negative_odd_number():
    assert check_even_odd(-5) == "Odd"
