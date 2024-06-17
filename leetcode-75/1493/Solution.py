class Solution:

    # Solução muito próxima do LeetCode 1004: Max Consecutive Ones III, com k fixado em 1 e a obrigatoriedade de remoção de um elemento

    def longestSubarray(self, nums: list[int]) -> int:
        
        i = longestPath = pathSum = 0
        
        for j in range(len(nums)):

            pathSum += nums[j]

            # Se o tamanho da janela possui uma soma menor ou igual (aqui entra o 1 possível a mais)
            # então é um candidato a maior caminho
            if j - i <= pathSum:
                longestPath = max(longestPath, pathSum)
            # Ao passo que, se a soma é maior que a própria janela, deve-se incrementar o ponteiro i
            else:
                pathSum -= nums[i]
                i += 1

        # Se 
        return longestPath if 0 in nums[i:j+1] else longestPath - 1