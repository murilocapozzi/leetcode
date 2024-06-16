import pytest
from Solution import Solution



def test_example1():

    nums = [1,3]
    n = 6

    output = Solution().minPatches(nums, n)

    assert output == 1

def test_example2():

    nums = [1,2,2]
    n = 5

    output = Solution().minPatches(nums, n)

    assert output == 1