class Solution:
    
    # Código estudado
    
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        totalFlips = 0
        
        # Flag que sinaliza o estado atual da operação de flip
        flagFlipped = 0
        
        # Lista que guarda em qual ponto flipou os k próximos
        fp = [0] * n

        for i in range(n):
            
            # Se i é maior ou igual a k, atualiza a flag com a operação guardada em fp[i-k] por um XOR
            if i >= k: flagFlipped ^= fp[i - k]
                
            # Verifica se o nums[i] precisa ser flipado ou não pela flag
            if flagFlipped == nums[i]:
                # Entrou neste if então precisa ser flipado
                
                # Se não existe espaço para flipar, não é possível resolver logo retorna -1
                if i + k > n: return -1

                # Concretiza o flip em i
                fp[i] = 1
                flagFlipped ^= 1
                totalFlips += 1

        return totalFlips