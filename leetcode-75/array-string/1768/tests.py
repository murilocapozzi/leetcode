import pytest
from Solution import Solution



def test_example1():

    word1 = "abc"
    word2 = "pqr"

    s = Solution()
    output = s.mergeAlternately(word1, word2)

    assert output == "apbqcr"

def test_example2():

    word1 = "ab"
    word2 = "pqrs"

    s = Solution()
    output = s.mergeAlternately(word1, word2)

    assert output == "apbqrs"

def test_example3():

    word1 = "abcd"
    word2 = "pq"

    s = Solution()
    output = s.mergeAlternately(word1, word2)

    assert output == "apbqcd"