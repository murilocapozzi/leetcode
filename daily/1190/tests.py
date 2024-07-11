import pytest
from Solution import Solution



def test_example1():

    s = "(abcd)"

    output = Solution().reverseParentheses(s)

    assert output == "dcba"

def test_example2():

    s = "(u(love)i)"

    output = Solution().reverseParentheses(s)

    assert output == "iloveu"

def test_example3():

    s = s = "(ed(et(oc))el)"

    output = Solution().reverseParentheses(s)

    assert output == "leetcode"