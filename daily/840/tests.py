import pytest
from Solution import Solution



def test_example1():

    difficulty = [2,4,6,8,10]
    profit = [10,20,30,40,50]
    worker = [4,5,6,7]

    output = Solution().maxProfitAssignment(difficulty, profit, worker)

    assert output == 100

def test_example2():

    difficulty = [85,47,57]
    profit = [24,66,99]
    worker = [40,25,25]

    output = Solution().maxProfitAssignment(difficulty, profit, worker)

    assert output == 0