import pytest
from Solution import Solution


def test_example1():

    head = Solution().arrToList([1,2,3,4,5])

    output = Solution().listToArr(Solution().reverseList(head))

    assert output == [5,4,3,2,1]

def test_example2():

    head = Solution().arrToList([1,2])

    output = Solution().listToArr(Solution().reverseList(head))

    assert output == [2,1]

def test_example3():

    head = Solution().arrToList([])

    output = Solution().listToArr(Solution().reverseList(head))

    assert output == []