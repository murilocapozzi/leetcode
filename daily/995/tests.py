import pytest
from Solution import Solution



def test_example1():

    nums = [0,1,0]
    k = 1

    output = Solution().minKBitFlips(nums, k)

    assert output == 2

def test_example2():

    nums = [1,1,0]
    k = 2

    output = Solution().minKBitFlips(nums, k)

    assert output == -1
    
def test_example3():

    nums = [0,0,0,1,0,1,1,0]
    k = 3

    output = Solution().minKBitFlips(nums, k)

    assert output == 3
    