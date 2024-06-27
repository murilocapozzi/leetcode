import pytest
from Solution import Solution



def test_example1():

    edges = [[1,2],[2,3],[4,2]]

    output = Solution().findCenter(edges)

    assert output == 2

def test_example2():

    edges = [[1,2],[5,1],[1,3],[1,4]]

    output = Solution().findCenter(edges)

    assert output == 1