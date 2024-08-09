import pytest
from Solution import Solution



def test_example1():

    names = ["Mary","John","Emma"]
    heights = [180,165,170]

    output = Solution().sortPeople(names, heights)

    assert output == ["Mary","Emma","John"]

def test_example2():

    names = ["Alice","Bob","Bob"]
    heights = [155,185,150]

    output = Solution().sortPeople(names, heights)

    assert output == ["Bob","Alice","Bob"]