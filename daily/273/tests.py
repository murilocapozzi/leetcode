import pytest
from Solution import Solution



def test_example1():

    nums = 123

    output = Solution().numberToWords(nums)

    assert output == "One Hundred Twenty Three"

def test_example2():

    nums = 12345

    output = Solution().numberToWords(nums)

    assert output == "Twelve Thousand Three Hundred Forty Five"
    
def test_example3():

    nums = 1234567

    output = Solution().numberToWords(nums)

    assert output == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"