class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        
        i = 0
        j = len(nums) - 1
        numOperations = 0
        # Ordena nums para conseguir varrer a lista da melhor forma
        # Consequência: o algoritmo torna-se O(nlgn)
        nums.sort()

        while i < j:
            result = nums[i] + nums[j]

            # Se o resultado é igual a k, incrementa numOperations e os dois ponteiros andam
            if result == k:
                numOperations += 1
                i += 1
                j -= 1
            # Se o resultado é maior que k, então precisamos decrementar no lado decrescente (j), para diminuir o valor e tentar igualar a k
            elif result > k:
                j -= 1
            # Se o resultado é menor que k, então precisamos incrementar no lado crescente (i), para auemntar o valor e tentar igualar a k
            else:
                i += 1

        return numOperations