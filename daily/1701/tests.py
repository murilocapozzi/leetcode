import pytest
from Solution import Solution



def test_example1():

    customers = [[1,2],[2,5],[4,3]]

    output = Solution().averageWaitingTime(customers)
    
    assert output == 5.00000

def test_example2():

    customers = [[5,2],[5,4],[10,3],[20,1]]
    
    output = Solution().averageWaitingTime(customers)
    
    assert output == 3.25000