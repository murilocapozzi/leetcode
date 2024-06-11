class Solution:
    def maxArea(self, height: list[int]) -> int:

        maxContainer = 0
        # Percorre a lista com dois ponteiros, um no início e outro no final
        i = 0
        j = len(height) - 1

        while i < j:

            actualContainer = 0

            # Confere qual das alturas é a menor, pois será a usado para multiplicar com o comprimento (j - i), incrementando caso for i, decrementando caso for j
            if height[i] > height[j]:
                actualContainer = height[j] * (j - i)
                j -= 1
            else:
                actualContainer = height[i] * (j - i)
                i += 1

            # Atualiza-se o maior contâiner calculado
            if actualContainer > maxContainer:
                maxContainer = actualContainer

        return maxContainer
            


        