import pytest
from Solution import Solution



def test_example1():

    nums = [5,2,3,1]

    output = Solution().sortArray(nums)
    sortedNums = sorted(nums)
    
    assert output == sortedNums

def test_example2():

    nums = [5,1,1,2,0,0]

    output = Solution().sortArray(nums)
    sortedNums = sorted(nums)
    
    assert output == sortedNums