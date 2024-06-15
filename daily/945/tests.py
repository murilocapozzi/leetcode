import pytest
from Solution import Solution



def test_example1():

    nums = [1,2,2]

    output = Solution().minIncrementForUnique(nums)

    assert output == 1

def test_example2():

    nums = [3,2,1,2,1,7]

    output = Solution().minIncrementForUnique(nums)

    assert output == 6