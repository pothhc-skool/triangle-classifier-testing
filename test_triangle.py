import math
from triangle import is_valid_triangle, classify_triangle

# Test that a triangle with three equal sides is classified as Equilateral
def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

# Test that a triangle with two equal sides is classified as Isosceles
def test_isosceles():
    assert classify_triangle(3, 3, 4) == "Isosceles"

# Test that a triangle with all different sides is classified as Scalene
def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"

# Test that an invalid triangle raises a ValueError
def test_invalid_triangle():
    assert classify_triangle(1, 2, 5) == "Invalid"

def test_right_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_degenerate_triangle():
    assert classify_triangle(4, 5, 9) == "Invalid"


def test_right_isosceles_noninteger():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"


def test_triangle_validity():
    assert is_valid_triangle(3, 4, 5) is True
    assert is_valid_triangle(1, 2, 3) is False