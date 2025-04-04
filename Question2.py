def calculate_average(*args):

    if not args:
        return None

    try:
        total = sum(args)
        count = len(args)
        return total / count
    except TypeError:
        raise TypeError("All arguments must be numbers")

print(calculate_average(1, 2, 3, 4))
print(calculate_average(10))
print(calculate_average())