class NegativeNumberError(Exception):

    def __init__(self, value):
        self.value = value
        self.message = f"Negative number detected: {value}"
        super().__init__(self.message)

def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    return f"Number {number} is positive or zero"

try:
    result1 = check_positive(5)
    print(result1)

    result2 = check_positive(0)
    print(result2)

    result3 = check_positive(-3)
    print(result3)

except NegativeNumberError as e:
    print(f"Caught an error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

try:
    check_positive(-10)
except NegativeNumberError as e:
    print(f"Caught another error: {e}")