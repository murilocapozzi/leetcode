import pytest
from Solution import Solution



def test_example1():

    nums = [0,1,0,3,12]

    Solution().moveZeroes(nums)

    assert nums == [1,3,12,0,0]

def test_example2():

    nums = [0]

    Solution().moveZeroes(nums)

    assert nums == [0]
