from exercise_2.bubble_sort import BubbleSort
from exercise_3.factorial_calculator import FactorialCalculator
from exercise_4.multiples_sum_calculator import MultiplesSumCalculator


class TestVotePercentage:

    def test_calculate_vote_percentage(self):
        total_voters = 1000
        blank_votes = 100
        null_votes = 50
        valid_votes = 850

        percent_blank = (blank_votes / total_voters) * 100
        percent_null = (null_votes / total_voters) * 100
        percent_valid = (valid_votes / total_voters) * 100

        assert percent_blank == 10.0
        assert percent_null == 5.0
        assert percent_valid == 85.0


class TestBubbleSort:

    def test_bubble_sort_order(self):
        numbers = [5, 1, 4, 2, 8]
        sorter = BubbleSort(numbers)
        sorter.sort()

        assert sorter.numbers == [1, 2, 4, 5, 8]

    def test_bubble_sort_main_runs(self):
        BubbleSort.main()
        assert True  # if not raises error, passed


class TestFactorial:

    def test_factorial_of_five(self):
        calculator = FactorialCalculator(5)
        assert calculator.calculate() == 120

    def test_factorial_of_zero(self):
        calculator = FactorialCalculator(0)
        assert calculator.calculate() == 1


class TestSumMultiples:

    def test_sum_multiples_below_ten(self):
        calculator = MultiplesSumCalculator(10)
        assert calculator.calculate() == 23

    def test_sum_multiples_below_twenty(self):
        calculator = MultiplesSumCalculator(20)
        assert calculator.calculate() == 78
