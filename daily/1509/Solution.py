from cmath import inf

class Solution:
    def minDifference(self, nums: list[int]) -> int:

        # Se possuir até 4 elementos, pode-se realizar 3 trocas de qualquer elemento
        # Logo a diferença será 0 sempre, já que serão números repetidos
        if len(nums) <= 4: return 0

        # Ordena para ter certeza dos menores e maiores elementos
        # O(nlgn)
        nums.sort()
        first3 = nums[:4]
        last3 = nums[-4:]

        # Analisam-se os três menores com os três maiores
        # De forma crescente, ou seja:
        #   primeiro com o antepenúltimo
        #   segundo com penúltimo
        #   terceiro com último
        # Com isso, registra-se a menor diferença que será repetida perdurada para outros elementos
        return min(last - first for first,last in zip(first3, last3))