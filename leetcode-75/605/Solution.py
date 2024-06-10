class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        # 0 =>  empty
        # 1 => not empty
        # 2 => planted

        size = len(flowerbed)

        for i in range(size):

            if flowerbed[i] == 0:

                if n == 0:
                    break
                    
                before = i - 1
                after = i + 1

                if before >= 0 and flowerbed[before] == 1:
                    continue

                if after < size and flowerbed[after] == 1:
                    continue

                flowerbed[i] += 1
                n -= 1


        return n == 0

        