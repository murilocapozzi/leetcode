import pytest
from Solution import Solution



def test_example1():

    n = 5
    k = 2

    output = Solution().findTheWinner(n, k)
    
    assert output == 3

def test_example2():

    n = 6
    k = 5

    output = Solution().findTheWinner(n, k)
    
    assert output == 1