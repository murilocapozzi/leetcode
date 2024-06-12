class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # Counting sort

        qtd = [0, 0, 0]

        # Descobre quantas vezes ocorre cada cor
        for num in nums: qtd[num] += 1

        nums.clear()

        # Preenche nums pela quantidade da ocorrência da cor em ordem crescente (i)
        for i in range(3): nums.extend([i] * qtd[i])

            