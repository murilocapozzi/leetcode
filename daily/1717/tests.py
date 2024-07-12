import pytest
from Solution import Solution



def test_example1():

    s = "cdbcbbaaabab"
    x = 4
    y = 5

    output = Solution().maximumGain(s, x, y)

    assert output == 19
    
def test_example2():

    s = "aabbaaxybbaabb"
    x = 5
    y = 4

    output = Solution().maximumGain(s, x, y)

    assert output == 20