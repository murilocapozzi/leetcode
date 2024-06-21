import pytest
from Solution import Solution



def test_example1():

    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    minutes = 3

    output = Solution().maxSatisfied(customers, grumpy, minutes)

    assert output == 16

def test_example2():

    customers = [1]
    grumpy = [0]
    minutes = 1

    output = Solution().maxSatisfied(customers, grumpy, minutes)

    assert output == 1