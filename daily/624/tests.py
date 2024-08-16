import pytest
from Solution import Solution



def test_example1():

    arrays = [[1,2,3],[4,5],[1,2,3]]

    output = Solution().maxDistance(arrays)

    assert output == 4

def test_example2():

    arrays = [[1],[1]]

    output = Solution().maxDistance(arrays)

    assert output == 0
