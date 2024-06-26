import pytest
from Solution import Solution



def test_example1():

    nums = [1,1,0,1]

    output = Solution().longestSubarray(nums)

    assert output == 3

def test_example2():

    nums = [0,1,1,1,0,1,1,0,1]

    output = Solution().longestSubarray(nums)

    assert output == 5

def test_example3():

    nums = [1,1,1]

    output = Solution().longestSubarray(nums)

    assert output == 2