from collections import Counter

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        # Conta a quantidade de elementos da lista e cria um dicionário, sendo a key o elemento e value a quantidade
        frequency = Counter(nums)
        
        # A função lambda retorna uma tupla, sendo:
        # 1) Ordena pela frequência, de forma crescente, que está no value
        # 2) Caso seja igual, ordena de forma decrescente pela key (o menor número, torna-se o maior e vice-versa)
        return sorted(nums, key=lambda x: (frequency[x], -x))