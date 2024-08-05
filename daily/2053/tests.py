import pytest
from Solution import Solution



def test_example1():

    arr = ["d","b","c","b","c","a"]
    k = 2

    output = Solution().kthDistinct(arr, k)

    assert output == "a"

def test_example2():

    arr = ["aaa","aa","a"]
    k = 1

    output = Solution().kthDistinct(arr, k)

    assert output == "aaa"
    
def test_example3():

    arr = ["a","b","a"]
    k = 3

    output = Solution().kthDistinct(arr, k)

    assert output == ""