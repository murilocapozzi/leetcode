from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radiant = deque()
        dire = deque()
        
        i = 0
        while i < len(senate):
            if senate[i] == 'R': radiant.append(i)
            else: dire.append(i)
            i += 1    
        
        while radiant and dire:
            i += 1
            
            # Quem tem a prioridade, mantém o senador
            if radiant[0] < dire[0]: radiant.append(i)
            else: dire.append(i)
            
            radiant.popleft()
            dire.popleft()
            
        # Retorna a party que possuir elementos ativos
        return 'Radiant' if radiant else 'Dire'