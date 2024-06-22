import pytest
from Solution import Solution



def test_example1():

    s = "leet**cod*e"

    output = Solution().removeStars(s)

    assert output == "lecoe"

def test_example2():

    s = "erase*****"

    output = Solution().removeStars(s)

    assert output == ""