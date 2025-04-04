def classify_number():
    while True:
        try:
            num = int(input("Please enter an integer: "))
            if num > 0:
                return "Positive"
            elif num < 0:
                return "Negative"
            else:
                return "Zero"
        except ValueError:
            print("That's not a valid integer. Please try again.")

result = classify_number()
print(f"The number is: {result}")