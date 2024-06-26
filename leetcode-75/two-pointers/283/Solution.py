class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        n = len(nums)
        i = 0
        j = 1

        while i < n:

            # Descobre onde está o próximo zero
            while i < n and nums[i] != 0:
                i += 1
                j += 1

            # Condição para evitar que o vetor já acabou e se sequer era um zero
            if i < n and nums[i] == 0:
                # Descobre onde está o próximo não zero para substituir
                while j < n and nums[j] == 0:
                    j += 1
                
                # Se existe um possível para substituir, faz a troca
                if j < n:
                    nums[i], nums[j] = nums[j], nums[i]
                    
            i += 1
        