import pytest
from Solution import Solution


def test_example1():

    head = Solution().arrToList([0,3,1,0,4,5,2,0])

    output = Solution().listToArr(Solution().mergeNodes(head))

    assert output == [4,11]

def test_example2():

    head = Solution().arrToList([0,1,0,3,0,2,2,0])

    output = Solution().listToArr(Solution().mergeNodes(head))

    assert output == [1,3,4]