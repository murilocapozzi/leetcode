import pytest
from Solution import Solution



def test_example1():

    nums = [1,1,2,1,1]
    k = 3

    output = Solution().numberOfSubarrays(nums, k)

    assert output == 2

def test_example2():

    nums = [2,4,6]
    k = 1

    output = Solution().numberOfSubarrays(nums, k)

    assert output == 0
    
def test_example3():

    nums = nums = [2,2,2,1,2,2,1,2,2,2]
    k = 2

    output = Solution().numberOfSubarrays(nums, k)

    assert output == 16