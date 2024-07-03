import pytest
from Solution import Solution



def test_example1():

    nums = [5,3,2,4]

    output = Solution().minDifference(nums)

    assert output == 0

def test_example2():

    nums = [1,5,0,10,14]

    output = Solution().minDifference(nums)

    assert output == 1
    
def test_example3():

    nums = [3,100,20]

    output = Solution().minDifference(nums)

    assert output == 0