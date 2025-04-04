def get_valid_number():
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)
            print(f"You entered a valid number: {number}")
            return number
        except ValueError:
            print("Error: That's not a valid number. Please enter a numeric value.")

if __name__ == "__main__":
    valid_number = get_valid_number()