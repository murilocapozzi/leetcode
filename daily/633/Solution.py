import math

class Solution:

    def isPerfect(self, c: int) -> bool:

        num = math.isqrt(c)

        return num * num == c

    def judgeSquareSum(self, c: int) -> bool:

        if self.isPerfect(c): return True

        i = 1
        maxRange = math.isqrt(c)

        while i <= maxRange:

            j = c - i * i

            if self.isPerfect(j):
                return True

            i += 1

        return False
        