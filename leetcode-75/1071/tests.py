import pytest
from Solution import Solution



def test_example1():

    str1 = "ABCABC"
    str2 = "ABC"

    s = Solution()
    output = s.gcdOfStrings(str1, str2)

    assert output == "ABC"

def test_example2():

    str1 = "ABABAB"
    str2 = "ABAB"

    s = Solution()
    output = s.gcdOfStrings(str1, str2)

    assert output == "AB"

def test_example3():

    str1 = "LEET"
    str2 = "CODE"

    s = Solution()
    output = s.gcdOfStrings(str1, str2)

    assert output == ""