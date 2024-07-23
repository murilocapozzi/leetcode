import pytest
from Solution import Solution



def test_example1():

    nums = [1,1,2,2,2,3]

    output = Solution().frequencySort(nums)

    assert output == [3,1,1,2,2,2]

def test_example2():

    nums = [2,3,1,3,2]

    output = Solution().frequencySort(nums)

    assert output == [1,3,3,2,2]
    
def test_example3():

    nums = [-1,1,-6,4,5,-6,1,4,1]

    output = Solution().frequencySort(nums)

    assert output == [5,-1,4,4,-6,-6,1,1,1]