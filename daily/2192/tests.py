import pytest
from Solution import Solution



def test_example1():

    n = 8
    edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

    output = Solution().getAncestors(n, edgeList)

    assert output == [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]

def test_example2():

    n = 5
    edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    output = Solution().getAncestors(n, edgeList)

    assert output == [[],[0],[0,1],[0,1,2],[0,1,2,3]]