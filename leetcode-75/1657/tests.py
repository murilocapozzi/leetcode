import pytest
from Solution import Solution



def test_example1():

    word1 = "abc"
    word2 = "bca"

    output = Solution().closeStrings(word1, word2)

    assert output == True

def test_example2():

    word1 = "a"
    word2 = "aa"

    output = Solution().closeStrings(word1, word2)

    assert output == True

def test_example3():

    word1 = "cabbba"
    word2 = "abbccc"

    output = Solution().closeStrings(word1, word2)

    assert output == True