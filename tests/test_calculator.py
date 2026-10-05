from src.calculator import add, subtract, multiply, divide

# Six assertions required by the slides
assert add(2, 3) == 5
assert add(-1, 1) == 0
assert subtract(10, 4) == 6
assert subtract(0, 0) == 0
assert multiply(3, 4) == 12
assert multiply(0, 99) == 0

# Negative numbers
assert add(-2, -3) == -5
assert subtract(-10, -4) == -6
assert multiply(-3, 4) == -12
assert divide(-10, 2) == -5

# Decimal numbers
assert add(1.5, 2.5) == 4.0
assert subtract(5.5, 2.5) == 3.0
assert multiply(1.5, 2.0) == 3.0
assert divide(5.0, 2.0) == 2.5

# Zero
assert add(0, 0) == 0
assert subtract(0, 0) == 0
assert multiply(0, 99) == 0
assert divide(0, 2) == 0

# Division by zero
try:
    divide(5, 0)
except ValueError:
    print("Division by zero correctly rejected.")
else:
    raise AssertionError("Expected ValueError for division by zero.")

print("All assertions passed.")
