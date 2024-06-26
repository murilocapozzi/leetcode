class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        

        longestPath, i, currentPath = 0, 0, 0

        for j in range(len(nums)):

            currentPath += nums[j]

            # "j - i" é o tamanho da janela de análise
            # currentPath, caminho atual, representa a soma dos valores de 1's achados dentro de j - i

            # Se esse tamanho, diminuído do caminho atual mais 1 for menor ou igual a k
                # Então representa um caminho possivelmente maior -> atualiza longestPath, o maior caminho visto
            # Se não, o ponteiro da esquerda é movido e retira-se do caminho atual
            if j - i - currentPath + 1 <= k:
                longestPath = max(longestPath, j - i + 1)
            else:
                currentPath -= nums[i]
                i += 1

        return longestPath