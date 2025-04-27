from factorial_calculator import FactorialCalculator

if __name__ == "__main__":
    number = 5  # You can change the number here if you want
    calculator = FactorialCalculator(number)
    result = calculator.calculate()

    print(f"The factorial of {number} is: {result}")
