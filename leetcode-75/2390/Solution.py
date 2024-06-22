class Solution:
    def removeStars(self, s: str) -> str:
        
        # Inicia a pilha
        stack = []
        
        for c in s:

            # Se for '*' remove o elemento na cabeça da pilha, senão insere
            if c == "*":
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)