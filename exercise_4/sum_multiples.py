from multiples_sum_calculator import MultiplesSumCalculator

if __name__ == "__main__":
    limit = 10  # You can change the limit here
    calculator = MultiplesSumCalculator(limit)
    result = calculator.calculate()

    print(f"The sum of all multiples of 3 or 5 below {limit} is: {result}")
