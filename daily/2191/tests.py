import pytest
from Solution import Solution



def test_example1():

    mapping = [8,9,4,0,2,1,3,5,7,6]
    nums = [991,338,38]

    output = Solution().sortJumbled(mapping, nums)

    assert output == [338,38,991]

def test_example2():

    mapping = [0,1,2,3,4,5,6,7,8,9]
    nums = [789,456,123]

    output = Solution().sortJumbled(mapping, nums)

    assert output == [123,456,789]
    