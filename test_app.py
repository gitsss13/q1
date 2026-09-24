from app import square, is_even

def test_square_positive():
    assert square(5) == 25

def test_square_zero():
    assert square(0) == 0

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(7) is False