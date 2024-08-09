import pytest
from Solution import Solution



def test_example1():

    matrix = [[3,7,8],[9,11,13],[15,16,17]]

    output = Solution().luckyNumbers(matrix)

    assert output == [15]

def test_example2():

    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]

    output = Solution().luckyNumbers(matrix)

    assert output == [12]
    
def test_example3():

    matrix = [[7,8],[1,2]]

    output = Solution().luckyNumbers(matrix)

    assert output == [7]