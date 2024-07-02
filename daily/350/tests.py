import pytest
from Solution import Solution



def test_example1():

    nums1 = [1,2,2,1]
    nums2 = [2,2]

    output = Solution().intersect(nums1, nums2)

    assert output == [2,2]

def test_example2():

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    output = Solution().intersect(nums1, nums2)

    assert output == [4,9]