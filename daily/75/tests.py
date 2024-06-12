import pytest
from Solution import Solution



def test_example1():

    nums = [2,0,2,1,1,0]

    Solution().sortColors(nums)

    assert nums == [0,0,1,1,2,2]

def test_example2():

    nums = [2,0,1]

    Solution().sortColors(nums)

    assert nums == [0,1,2]