import pytest
from Solution import Solution



def test_example1():

    height = [1,8,6,2,5,4,8,3,7]

    output = Solution().maxArea(height)

    assert output == 49

def test_example2():

    height = [1,1]

    output = Solution().maxArea(height)

    assert output == 1
