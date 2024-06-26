class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        # Lista que mantém os asteróides definitivos indo para a esquerda, sem colisões iminentes
        left_asteroids = []
        
        # Lista que mantém os asteróides indo para direita, que podem sofrer colisão de novos asteróides
        state = []
        
        for asteroid in asteroids:
            
            if asteroid > 0:
            # Se está indo para a direita, pode ser colocado sem análise em state
                state.append(asteroid)
                continue
                
            while state:
            # Analisa cada asteróide de state possível para colidir
                enemy = state.pop()
                
                if abs(asteroid) == enemy:
                # Se é igual, quebra o de state e não insere o novo
                    break
                
                if abs(asteroid) < enemy:
                # Se é menor, re-insere o analisado e para a análise sem inserir o novo
                    state.append(enemy)
                    break
            else:
            # Se não existe asteróide em state OU
            # Se foi maior que asteróides armazenados em state,
            #   o asteróide negativo é armazenado definitivo em left_asteroids
                left_asteroids.append(asteroid)

        # Junta os asteróides negativos definitivos e os remanescentes de state
        return left_asteroids + state