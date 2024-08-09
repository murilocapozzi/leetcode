import pytest
from Solution import Solution


def test_example1():

    head = Solution().arrToList([3,1])

    output = Solution().nodesBetweenCriticalPoints(head)

    assert output == [-1,-1]

def test_example2():

    head = Solution().arrToList([5,3,1,2,5,1,2])

    output = Solution().nodesBetweenCriticalPoints(head)

    assert output == [1,3]

def test_example3():

    head = Solution().arrToList([1,3,2,2,3,2,2,2,7])

    output = Solution().nodesBetweenCriticalPoints(head)

    assert output == [3,3]