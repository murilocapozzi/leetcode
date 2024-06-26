import pytest
from Solution import Solution


def test_example1():

    chars = ["a","a","b","b","c","c","c"]

    output = Solution().compress(chars)

    assert output == 6
    assert chars == ["a","2","b","2","c","3"]

def test_example2():

    chars = ["a"]

    output = Solution().compress(chars)

    assert output == 1
    assert chars == ["a"]

def test_example3():

    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

    output = Solution().compress(chars)

    assert output == 4
    assert chars == ["a","b","1","2"]