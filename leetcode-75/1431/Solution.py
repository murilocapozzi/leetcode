class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        return [kid + extraCandies >= max(candies) for kid in candies]