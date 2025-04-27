from typing import List


class BubbleSort:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def sort(self) -> List[int]:
        n = len(self.numbers)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
        return self.numbers

    def main():
        numbers = [5, 3, 2, 4, 7, 1, 0, 6]
        sorter = BubbleSort(numbers)
        sorted_numbers = sorter.sort()
        print(f"Original list: {numbers}")
        print(f"Sorted list: {sorted_numbers}")

    if __name__ == "__main__":
        main()
