import pytest
from Solution import Solution



def test_example1():

    s = "3[a]2[bc]"

    output = Solution().decodeString(s)

    assert output == "aaabcbc"

def test_example2():

    s = s = "3[a2[c]]"

    output = Solution().decodeString(s)

    assert output == "accaccacc"

def test_example3():

    s = "2[abc]3[cd]ef"

    output = Solution().decodeString(s)

    assert output == "abcabccdcdcdef"