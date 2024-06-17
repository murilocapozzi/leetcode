import pytest
from Solution import Solution



def test_example1():

    c = 5

    output = Solution().judgeSquareSum(c)

    assert output == True

def test_example2():

    c = 3

    output = Solution().judgeSquareSum(c)

    assert output == False

def test_example3():

    c = 4

    output = Solution().judgeSquareSum(c)

    assert output == True

def test_example4():

    c = 0

    output = Solution().judgeSquareSum(c)

    assert output == True