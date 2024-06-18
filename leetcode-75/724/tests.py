import pytest
from Solution import Solution


def test_example1():

    nums = [1,7,3,6,5,6]

    output = Solution().pivotIndex(nums)

    assert output == 3

def test_example2():

    nums = [1,2,3]

    output = Solution().pivotIndex(nums)

    assert output == -1

def test_example3():

    nums = [2,1,-1]

    output = Solution().pivotIndex(nums)

    assert output == 0