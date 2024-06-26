import pytest
from Solution import Solution


def test_example1():

    candies = [2,3,5,1,3]
    extraCandies = 3

    s = Solution()
    output = s.kidsWithCandies(candies, extraCandies)

    assert output == [True,True,True,False,True]

def test_example2():

    candies = [4,2,1,1,2]
    extraCandies = 1

    s = Solution()
    output = s.kidsWithCandies(candies, extraCandies)

    assert output == [True,False,False,False,False]

def test_example3():

    candies = [12, 1, 12]
    extraCandies = 10

    s = Solution()
    output = s.kidsWithCandies(candies, extraCandies)

    assert output == [True,False,True]