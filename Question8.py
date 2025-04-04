import random

def generate_random_numbers(count, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(count)]


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Main program
def main():
    random_numbers = generate_random_numbers(10, 1, 100)

    avg = calculate_average(random_numbers)

    print("Generated random numbers:", random_numbers)
    print(f"Average of the numbers: {avg:.2f}")


if __name__ == "__main__":
    main()