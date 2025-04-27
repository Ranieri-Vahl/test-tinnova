from multiples_sum_calculator import MultiplesSumCalculator


def main():
    while True:
        try:
            user_input = input("Enter a non-negative integer to calculate the sum of multiples of 3 or 5 (or 'q' to quit): ")

            if user_input.lower() == 'q':
                print("Goodbye!")
                break

            limit = int(user_input)

            if limit < 0:
                print("Please enter a non-negative integer.\n")
                continue

            calculator = MultiplesSumCalculator(limit)
            result = calculator.calculate()
            print(f"The sum of all multiples of 3 or 5 below {limit} is: {result}\n")

        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.\n")


if __name__ == "__main__":
    main()
