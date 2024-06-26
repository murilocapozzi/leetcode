import pytest
from Solution import Solution



def test_example1():

    gain = [-5,1,5,0,-7]

    output = Solution().largestAltitude(gain)

    assert output == 1

def test_example2():

    gain = [-4,-3,-2,-1,4,3,2]

    output = Solution().largestAltitude(gain)

    assert output == 0
