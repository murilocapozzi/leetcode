import pytest
from Solution import Solution



def test_example1():

    grid = [[3,2,1],[1,7,6],[2,7,7]]

    output = Solution().equalPairs(grid)

    assert output == 1

def test_example2():

    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

    output = Solution().equalPairs(grid)

    assert output == 3
