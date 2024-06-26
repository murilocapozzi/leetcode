import pytest
from Solution import Solution



def test_example1():

    s = "abciiidef"
    k = 3

    output = Solution().maxVowels(s, k)

    assert output == 3

def test_example2():

    s = "aeiou"
    k = 2

    output = Solution().maxVowels(s, k)

    assert output == 2
    
def test_example3():

    s = "leetcode"
    k = 3

    output = Solution().maxVowels(s, k)

    assert output == 2