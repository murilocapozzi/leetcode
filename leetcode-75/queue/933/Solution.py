from collections import deque

class RecentCounter:

    def __init__(self):
        # Deque pode inserir e remover dos dois lados
        # Porém, restringe-se para criar uma fila
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Insere na direita
        self.queue.append(t)

        while self.queue[0] < t - 3000:
        # Remove os que estiverem fora do range, pela esquerda
            self.queue.popleft()

        return len(self.queue)