# test_main.py
import pytest
from main import add, subtract, multiply, divide, modulus, factorial, square

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(-9, 3) == -3
    assert divide(-9, -3) == 3
    assert divide(9, 0) == "Division by zero is not allowed"

def test_modulus():
    assert modulus(9, 4) == 1
    assert modulus(9, 0) == "Modulus by zero is not allowed"

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) == "Factorial of negative numbers is not allowed!"

def test_square():
    assert square(5) == 25
    assert square(-1) == 1
    assert square(0) == 0

