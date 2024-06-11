import pytest
from Solution import Solution



def test_example1():

    nums = [1,2,3,4]
    k = 5

    output = Solution().maxOperations(nums, k)

    assert output == 2

def test_example2():

    nums = [3,1,3,4,3]
    k = 6

    output = Solution().maxOperations(nums, k)

    assert output == 1
