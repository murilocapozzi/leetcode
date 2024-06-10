import pytest
from Solution import Solution



def test_example1():

    nums = [1,2,3,4,5]

    output = Solution().increasingTriplet(nums)

    assert output == True

def test_example2():

    nums = [5,4,3,2,1]

    output = Solution().increasingTriplet(nums)

    assert output == False

def test_example3():

    nums = [2,1,5,0,4,6]

    output = Solution().increasingTriplet(nums)

    assert output == True