import pytest
from Solution import Solution



def test_example1():

    bloomDay = [1,10,3,10,2]
    m = 3
    k = 1

    output = Solution().minDays(bloomDay, m, k)

    assert output == 3

def test_example2():

    bloomDay = [1,10,3,10,2]
    m = 3
    k = 2

    output = Solution().minDays(bloomDay, m, k)

    assert output == -1
    
def test_example3():

    bloomDay = [7,7,7,7,12,7,7]
    m = 2
    k = 3

    output = Solution().minDays(bloomDay, m, k)

    assert output == 12