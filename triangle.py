
import math


def is_valid_triangle(a, b, c) -> bool:
    # All three sides must be positive.
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # The sum of any two sides must exceed the third.
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True


def classify_triangle(a, b, c) -> str:
    # Check validity before classifying.
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    # Determine the triangle type.
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check whether the triangle is a right triangle.
    sides = sorted([a, b, c])
    x, y, hypotenuse = sides

    is_right = math.isclose(
        (x / hypotenuse) ** 2 + (y / hypotenuse) ** 2,
        1.0,
        rel_tol=1e-9,
        abs_tol=1e-12
    )

    if is_right:
        return "Right " + triangle_type

    return triangle_type
