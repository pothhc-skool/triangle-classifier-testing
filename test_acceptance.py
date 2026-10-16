import math
from triangle import classify_triangle

def test_stained_glass_customer_requirements():
    assert classify_triangle(6, 6, 6) == "Equilateral"
    assert classify_triangle(5, 5, 8) == "Isosceles"
    assert classify_triangle(4, 5, 9) == "Invalid"
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"