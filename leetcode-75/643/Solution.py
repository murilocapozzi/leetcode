class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        i = 0
        # Inicializa com os k primeiros somados
        maxAverage = average_ik = sum(nums[:k])
            
        # Com isso, o for inicializa em k
        for i in range(k, len(nums)):

            # Para evitar somas repetidas, apenas soma o novo nums[i] e retira o nums[i - k]
            average_ik += nums[i] - nums[i - k]

            if average_ik > maxAverage:
                maxAverage = average_ik

        # A média só é feita no final, já que a divisão iria ser inútil se feita todas as vezes
        return maxAverage / k
