class MultiplesSumCalculator:
    def __init__(self, limit: int):
        self.limit = limit

    def calculate(self) -> int:
        total = 0
        for i in range(self.limit):
            if i % 3 == 0 or i % 5 == 0:
                total += i
        return total
