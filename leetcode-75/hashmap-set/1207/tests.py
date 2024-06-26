import pytest
from Solution import Solution


def test_example1():

    arr = [1,2,2,1,1,3]

    output = Solution().uniqueOccurrences(arr)

    assert output == True

def test_example2():

    arr = [1,2]

    output = Solution().uniqueOccurrences(arr)

    assert output == False
    
def test_example3():

    arr = [1,2,2,1,1,3]

    output = Solution().uniqueOccurrences(arr)

    assert output == True

