# Triangle Classifier — Testing

## Project Overview

This project implements a triangle classifier in Python that determines whether three side lengths form a valid triangle and classifies the resulting shape.

The program identifies Equilateral, Isosceles, and Scalene triangles, including right-angle classifications. Invalid triangles return `"Invalid"`.

The project uses pytest for automated testing and GitHub Copilot to assist with generating unit tests.

## Installation and Running Tests

**Requirements:**
- Python 3.10 or later
- pytest

Install the required dependency:

```bash
py -m pip install -r requirements.txt
```

Run all tests:

```bash
py -m pytest -v
```

Run only the unit tests:

```bash
py -m pytest test_triangle.py -v
```

Run only the acceptance test:

```bash
py -m pytest test_acceptance.py -v
```

**Test results:** 9 tests passed (8 unit tests and 1 acceptance test).

## Equivalence Classes and Boundary Values

The following equivalence classes were identified from the triangle classification specification.

| Equivalence Class | Example Input | Expected Result |
|---|---|---|
| Equilateral | (5, 5, 5) | Equilateral |
| Isosceles | (5, 5, 6) | Isosceles |
| Scalene | (4, 5, 6) | Scalene |
| Right Scalene | (3, 4, 5) | Right Scalene |
| Right Isosceles | (5, 5, 5 × √2) | Right Isosceles |
| Invalid: triangle inequality fails | (1, 2, 5) | Invalid |
| Invalid: degenerate triangle | (4, 5, 9) | Invalid |
| Invalid: zero-length side | (0, 4, 5) | Invalid |

### Boundary Value Analysis

The program checks whether the sum of two sides is strictly greater than the third side.

For example:

- (4, 5, 8): Valid, because 4 + 5 > 8.
- (4, 5, 9): Invalid, because 4 + 5 = 9.
- (4, 5, 10): Invalid, because 4 + 5 < 10.

The program also rejects zero and negative side lengths.

Right-triangle classification uses floating-point tolerance instead of requiring exact equality. This is important for triangles with non-integer side lengths.

## Copilot Review Log

During unit testing, generated test assertions were reviewed against the assignment specification rather than accepted solely because they matched the program's current behavior.

| Test | Copilot Suggested? | Decision | Reason |
|------|--------------------|----------|--------|
| test_scalene | Yes | Edited | The original test expected `"Scalene"` for (3, 4, 5), but this is a right triangle. The test input was changed to (4, 5, 6). |
| test_invalid_triangle | Yes | Edited | The original test expected a ValueError, but the specification requires the return value `"Invalid"`. The assertion was corrected. |

## Acceptance Criteria

The stained-glass studio's requirements were translated into three measurable acceptance criteria:

1. **Shape classification:** Given three positive side lengths that satisfy the triangle inequality, the classifier returns the correct triangle classification.
2. **Invalid input handling:** Given invalid side lengths, including zero-length sides and degenerate triangles, the classifier returns `"Invalid"` without raising an exception.
3. **Right-angle identification:** Given a valid right triangle, including one with non-integer side lengths, the classifier returns a classification prefixed with `"Right "`.

### Acceptance Test

The acceptance test is implemented in `test_acceptance.py`.

It calls `classify_triangle()` using representative customer inputs and verifies the expected classifications and invalid-input behavior.

The acceptance test passed.

## Why an Equilateral Triangle Cannot Be Right

An equilateral triangle has three interior angles of 60 degrees. A right triangle requires one 90-degree angle, so an equilateral triangle cannot also be a right triangle.

## AI-Use Disclosure

GitHub Copilot was used to assist with generating unit tests in `test_triangle.py`. Its suggestions were reviewed against the written specification, and incorrect assertions were corrected.

Ollama was used for basic code implementation and breaking down the material into more concise sections.

The customer acceptance test was written and checked separately without GitHub Copilot or any A.I assistance.

All nine automated tests passed locally using pytest.