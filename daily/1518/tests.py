import pytest
from Solution import Solution



def test_example1():

    numBottles = 9
    numExchange = 3

    output = Solution().numWaterBottles(numBottles, numExchange)

    assert output == 13

def test_example2():

    numBottles = 15
    numExchange = 4

    output = Solution().numWaterBottles(numBottles, numExchange)

    assert output == 19