class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        equals = set(nums1) & set(nums2)
        output = []

        output.append(list(equals ^ set(nums1)))
        output.append(list(equals ^ set(nums2)))

        return output
        