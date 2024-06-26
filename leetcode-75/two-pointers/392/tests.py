import pytest
from Solution import Solution



def test_example1():

    s = "abc"
    t = "ahbgdc"

    output = Solution().isSubsequence(s, t)

    assert output == True

def test_example2():

    s = "axc"
    t = "ahbgdc"

    output = Solution().isSubsequence(s, t)

    assert output == False
