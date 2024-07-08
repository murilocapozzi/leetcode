class DPSolution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # Problema de Josefo
        # Determinar a posição final da última pessoa após eliminações em círculo
        
        res = 0
        
        # Começa em 2 pois anteriores resultam em 0, logo inútil processar
        for player_num in range(2, n + 1):
            res = (res + k) % player_num
            
        return res + 1