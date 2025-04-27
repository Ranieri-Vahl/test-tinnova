from factorial_calculator import FactorialCalculator


def main():
    while True:
        try:
            user_input = input("Enter a non-negative integer to calculate its factorial (or 'q' to quit): ")

            if user_input.lower() == 'q':
                print("Goodbye!")
                break

            number = int(user_input)

            if number < 0:
                print("Factorial is not defined for negative numbers.\n")
                continue

            calculator = FactorialCalculator(number)
            result = calculator.calculate()
            print(f"The factorial of {number} is: {result}\n")

        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.\n")


if __name__ == "__main__":
    main()
