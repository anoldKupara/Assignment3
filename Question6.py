def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers")
        return None

# Test cases
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers("10", 2))
print(divide_numbers(15, 3))
print(divide_numbers(5, "2"))