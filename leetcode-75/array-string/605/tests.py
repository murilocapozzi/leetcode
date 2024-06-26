import pytest
from Solution import Solution



def test_example1():

    flowerbed = [1,0,0,0,1]
    n = 1

    s = Solution()
    output = s.canPlaceFlowers(flowerbed, n)

    assert output == True

def test_example2():

    flowerbed = [1,0,0,0,1]
    n = 2

    s = Solution()
    output = s.canPlaceFlowers(flowerbed, n)

    assert output == False