class RecursionSolution:
    def findTheWinner(self, n: int, k: int) -> int:


        def recursion(n: int, k: int) -> int:
            # Caso base retorna 0 (o primeiro)
            # Se não é o caso base, reduz o problema em (n - 1, k)
            return 0 if n == 1 else (recursion(n - 1, k) + k) % n

        return recursion(n, k) + 1