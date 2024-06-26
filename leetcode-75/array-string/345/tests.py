import pytest
from Solution import Solution



def test_example1():

    s = "hello"

    output = Solution().reverseVowels(s)

    assert output == "holle"

def test_example2():

    s = "leetcode"

    output = Solution().reverseVowels(s)

    assert output == "leotcede"