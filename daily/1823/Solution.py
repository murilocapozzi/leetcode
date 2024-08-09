from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # Fila circular
        friends = deque(i+1 for i in range(n))
        counter = 1

        # Executa enquanto houver mais de 1 participante
        while len(friends) > 1:
            
            # Retira o primeiro
            friend = friends.popleft()
            
            if counter >= k:
                # Se bateu o contador, reinicia e o amigo da vez perde
                counter = 1
            else:
                # Ainda está contando, re-insere o amigo na fila e incrementa contador
                friends.append(friend)
                counter += 1

        # Retorna o único que sobrou
        return friends[0]
        