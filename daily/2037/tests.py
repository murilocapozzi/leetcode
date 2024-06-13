import pytest
from Solution import Solution



def test_example1():

    seats = [3,1,5]
    students = [2,7,4]

    output = Solution().minMovesToSeat(seats, students)

    assert output == 4

def test_example2():

    seats = [4,1,5,9]
    students = [1,3,2,6]

    output = Solution().minMovesToSeat(seats, students)

    assert output == 7
    
def test_example3():

    seats = [2,2,6,6]
    students = [1,3,2,6]

    output = Solution().minMovesToSeat(seats, students)

    assert output == 4