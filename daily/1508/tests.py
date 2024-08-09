import pytest
from Solution import Solution



def test_example1():

    nums = [1,2,3,4]
    n = 4
    left = 1
    right = 5

    output = Solution().rangeSum(nums, n, left, right)

    assert output == 13

def test_example2():

    nums = [1,2,3,4]
    n = 4
    left = 3
    right = 4

    output = Solution().rangeSum(nums, n, left, right)

    assert output == 6
    
def test_example3():

    nums = [1,2,3,4]
    n = 4
    left = 1
    right = 10

    output = Solution().rangeSum(nums, n, left, right)

    assert output == 50