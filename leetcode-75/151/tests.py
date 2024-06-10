import pytest
from Solution import Solution



def test_example1():

    s = "the sky is blue"

    output = Solution().reverseWords(s)

    assert output == "blue is sky the"

def test_example2():

    s = "  hello world  "

    output = Solution().reverseWords(s)

    assert output == "world hello"

def test_example3():

    s = "a good   example"

    output = Solution().reverseWords(s)

    assert output == "example good a"