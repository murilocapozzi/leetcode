import pytest
from Solution import Solution



def test_example1():

    nums1 = [1,2,3]
    nums2 = [2,4,6]

    output = Solution().findDifference(nums1, nums2)

    assert output == [[1,3],[4,6]]

def test_example2():

    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]

    output = Solution().findDifference(nums1, nums2)

    assert output == [[3],[]]
