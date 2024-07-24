class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
    
        # Dicionário que irá ter como key o número original e como value o novo obtido pelo mapeamento
        jumble = {}

        for num in nums:

            s = str(num)
            jumbledNum = 0

            # Itera sobre o número e descobre o novo 
            for c in s:
                jumbledNum = (jumbledNum * 10) + mapping[int(c)]
                
            jumble[num] = jumbledNum

        # Ordena nums com comparador sendo obtido pelo value do dicionário
        return sorted(nums, key=jumble.get)