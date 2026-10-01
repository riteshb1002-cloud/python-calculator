# Calculator CLI App
# Python Developer Internship - Task 1


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def calculator():
    """Main calculator function."""

    while True:
        print("\n===== CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                result = divide(num1, num2)

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numbers only.")


# Start the calculator
if __name__ == "__main__":
    calculator()