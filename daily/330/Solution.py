class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        
        # Mesma lógica para cálculo de troco de centavos

        miss = 1
        patches = 0
        i = 0

        while miss <= n: # Enquanto o "erro" for menor que o esperado, continue

            # Se o erro "cabe" dentro de nums[i], então acrescenta ao erro e vê o próximo
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # Enquanto o erro não couber em nums[i], ele dobra e incrementa o número de patches, ou seja
                # O mínimo necessário para solucionar o problema
                miss += miss
                patches += 1

        return patches