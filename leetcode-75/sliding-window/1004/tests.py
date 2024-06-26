import pytest
from Solution import Solution



def test_example1():

    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2

    output = Solution().longestOnes(nums, k)

    assert output == 6

def test_example2():

    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3

    output = Solution().longestOnes(nums, k)

    assert output == 10
