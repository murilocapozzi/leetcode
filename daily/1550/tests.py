import pytest
from Solution import Solution



def test_example1():

    arr = [2,6,4,1]

    output = Solution().threeConsecutiveOdds(arr)

    assert output == False

def test_example2():

    arr = [1,2,34,3,4,5,7,23,12]

    output = Solution().threeConsecutiveOdds(arr)

    assert output == True