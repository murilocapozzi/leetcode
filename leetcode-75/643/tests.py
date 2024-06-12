import pytest
from Solution import Solution



def test_example1():

    nums = [1,12,-5,-6,50,3]
    k = 4

    output = Solution().findMaxAverage(nums, k)

    assert output == 12.75000

def test_example2():

    nums = [5]
    k = 1

    output = Solution().findMaxAverage(nums, k)

    assert output == 5.00000
