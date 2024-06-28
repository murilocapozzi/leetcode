import pytest
from Solution import Solution


def test_example1():

    head = Solution().arrToList([1,3,4,7,1,2,6])

    output = Solution().listToArr(Solution().deleteMiddle(head))

    assert output == [1,3,4,1,2,6]

def test_example2():

    head = Solution().arrToList([1,2,3,4])

    output = Solution().listToArr(Solution().deleteMiddle(head))

    assert output == [1,2,4]
    
def test_example3():

    head = Solution().arrToList([2, 1])

    output = Solution().listToArr(Solution().deleteMiddle(head))

    assert output == [2]