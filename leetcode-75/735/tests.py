import pytest
from Solution import Solution



def test_example1():

    asteroids = [5,10,-5]

    output = Solution().asteroidCollision(asteroids)

    assert output == [5, 10]

def test_example2():

    asteroids = [8,-8]

    output = Solution().asteroidCollision(asteroids)

    assert output == []

def test_example3():

    asteroids = [10,2,-5]

    output = Solution().asteroidCollision(asteroids)

    assert output == [10]