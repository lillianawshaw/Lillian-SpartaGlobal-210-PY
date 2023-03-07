import pytest

from simple_calc import *

def test_add():
    assert add(3,5) == 8

def test_sub():
    assert sub(8,5) == 3


def test_string_add():
    assert string_add('') == 0
    assert string_add('1,2') == 3
    with pytest.raises(ValueError): #, match="invalid literal for int() with base 10: ''"):
        string_add('1,2,')


def test_password():
    assert Password("Password") == "Password must have two or more numbers\n"
    assert Password("password") == "Password must have two or more numbers\n" + "Password must have one or more capital letters\n"

def test_sum():
    assert sum(15) == 'Fizz Bang'
    assert sum(5) == 'Bang'
    assert sum(9) == 'Fizz '
    assert sum(11) == '11'



@pytest.mark.parametrize('num1, num2, expected', [(2,2,4),(5,5,10)])
def test_add_params(num1, num2, expected):
    assert add(num1, num2 ) == expected