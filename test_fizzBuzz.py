from fizzBuzz import fizzBuzz

def test_one_returns_one():
    assert fizzBuzz(1) == 1

def test_two_returns_two():
    assert fizzBuzz(2) == 2

def test_three_returns_fizz():
    assert fizzBuzz(3) == 'fizz'

def test_four_returns_four():
    assert fizzBuzz(4) == 4

def test_six_returns_fizz():
    assert fizzBuzz(6) == 'fizz'
    
def test_nine_returns_fizz():
    assert fizzBuzz(9) == 'fizz'

def test_five_returns_buzz():
    assert fizzBuzz(5) == 'buzz'
    
def test_ten_returns_buzz():
    assert fizzBuzz(10) == 'buzz'

def test_fifteen_returns_fizzbuzz():
    assert fizzBuzz(15) == 'fizzbuzz'