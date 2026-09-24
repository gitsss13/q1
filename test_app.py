from app import square, is_even

def test_square_positive():
    assert square(3) == 9
    assert square(5) == 25

def test_square_zero_and_negative():
    assert square(0) == 0
    assert square(-4) == 16

def test_is_even_true():
    assert is_even(2) is True
    assert is_even(10) is True

def test_is_even_false():
    assert is_even(3) is False
    assert is_even(9) is False