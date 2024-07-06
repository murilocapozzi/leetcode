import pytest
from Solution import Solution



def test_example1():

    n = 4
    time = 5

    output = Solution().passThePillow(n, time)

    assert output == 2

def test_example2():

    n = 3
    time = 2

    output = Solution().passThePillow(n, time)

    assert output == 3