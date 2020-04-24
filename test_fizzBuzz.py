from fizzBuzz import fizzBuzz

def test_one_returns_one():
    assert fizzBuzz(1) == 1

def test_two_returns_two():
    assert fizzBuzz(2) == 2

def test_three_returns_fizz():
    assert fizzBuzz(3) == 'fizz'

def test_four_returns_four():
    assert fizzBuzz(4) == 4