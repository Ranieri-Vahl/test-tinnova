class FactorialCalculator:
    def __init__(self, number: int):
        self.number = number

    def calculate(self) -> int:
        if self.number == 0:
            return 1

        result = 1
        for i in range(1, self.number + 1):
            result *= i
        return result
