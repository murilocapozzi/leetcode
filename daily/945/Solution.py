class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        
        if not nums: return 0

        nums = sorted(nums)
        moves = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            
            num = nums[i]

            # Prev guarda o "marco" a ser superado caso este seja maior ou igual que nums[i], sendo prev incrementado
            # Com isso, soma-se ao moves essa diferença
            if num <= prev:
                prev += 1
                moves += prev - num
            else:
                prev = num

        return moves