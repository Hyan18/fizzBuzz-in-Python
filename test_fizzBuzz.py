from fizzBuzz import fizzBuzz

import pytest

@pytest.mark.parametrize("n", [1, 2, 4, 7, 11])
def test_returns_number_itself(n):
    assert fizzBuzz(n) == n

@pytest.mark.parametrize("n", [3, 6, 9, 12, 18])
def test_has_factor_3_returns_fizz(n):
    assert fizzBuzz(n) == 'fizz'

@pytest.mark.parametrize("n", [5, 10, 20, 25, 35])
def test_has_factor_5_returns_buzz(n):
    assert fizzBuzz(n) == 'buzz'

@pytest.mark.parametrize("n", [15, 30, 45, 60, 75])
def test_has_factor_15_returns_fizzbuzz(n):
    assert fizzBuzz(n) == 'fizzbuzz'
