import pytest
from Solution import Solution


def test_example1():

    head = Solution().arrToList([1,2,3,4,5])

    output = Solution().listToArr(Solution().oddEvenList(head))

    assert output == [1,3,5,2,4]

def test_example2():

    head = Solution().arrToList([2,1,3,5,6,4,7])

    output = Solution().listToArr(Solution().oddEvenList(head))

    assert output == [2,3,6,7,1,5,4]