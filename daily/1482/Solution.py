class Solution:
    def canMakeBouquets(self, bloomDay: list[int], m: int, k: int, day: int) -> bool:
        
        # Retorna se podem ser feitos 'm' buquês até 'day'
        bouquets = flowers = 0
        
        for b in bloomDay:
            if b <= day:
                flowers += 1
                
                # Se existem 'k' flores que brotaram consecutivas, é possível fazer um buquê
                # 'flowers' zera se fez um buquê ou se a sequência parou sem sucesso
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
                
            if bouquets >= m:
                return True
    
        return False
    
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        
        # Se 'm * k' ultrapassa o próprio vetor 'bloomDay', não é possível realizar a lógica, -1
        if m * k > len(bloomDay): return -1
        
        # Busca binária pelo dia que é possível encontrar 'm' buquês
        low, high = min(bloomDay), max(bloomDay)
        
        while low < high:
            mid = (low + high) // 2
            
            if self.canMakeBouquets(bloomDay, m, k, mid):
                high = mid
            else:
                low = mid + 1
                
        return low