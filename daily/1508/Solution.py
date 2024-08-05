class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:

        sums = []
        i = 0
        ans = 0

        while i < n:
            j = i + 1
            sums.append(nums[i])
            while j < n:
                sums.append(sum(nums[i:j + 1]))
                j += 1
            i += 1

        sums.sort()

        for i in range(left - 1, right):
            ans += sums[i]

        return ans % (10**9 + 7)