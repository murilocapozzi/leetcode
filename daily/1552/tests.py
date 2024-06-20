import pytest
from Solution import Solution



def test_example1():

    position = [1,2,3,4,7]
    m = 3

    output = Solution().maxDistance(position, m)

    assert output == 3

def test_example2():

    position = [5,4,3,2,1,1000000000]
    m = 2

    output = Solution().maxDistance(position, m)

    assert output == 999999999