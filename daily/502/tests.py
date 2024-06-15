import pytest
from Solution import Solution



def test_example1():

    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]

    output = Solution().findMaximizedCapital(k, w, profits, capital)

    assert output == 4

def test_example2():

    k = 3
    w = 0
    profits = [1,2,3]
    capital = [0,1,2]

    output = Solution().findMaximizedCapital(k, w, profits, capital)

    assert output == 6