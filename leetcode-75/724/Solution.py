class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        # Caso base, não há o que comparar, sempre será verdade
        if len(nums) == 1: return 0

        # Mantém a soma da esquerda e a soma da direita em left e right respectivamente
        left = 0
        right = sum(nums[1:])

        for i in range(1, len(nums)):

            if left == right:
                return i - 1
            
            # Adiciona à esquerda o pivô (i - 1) e remove da direita o próximo pivô
            left += nums[i - 1]
            right -= nums[i]
        
        # Simétrico ao início para caso seja pivô na última posição
        if left == 0:
            return len(nums) - 1

        return -1