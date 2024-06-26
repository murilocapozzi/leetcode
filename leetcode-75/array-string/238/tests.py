import pytest
from Solution import Solution


def test_example1():

    nums = [1,2,3,4]

    output = Solution().productExceptSelf(nums)

    assert output == [24,12,8,6]

def test_example2():

    nums = [-1,1,0,-3,3]

    output = Solution().productExceptSelf(nums)

    assert output == [0,0,9,0,0]

