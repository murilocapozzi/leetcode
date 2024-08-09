class Solution:
    def minOperations(self, logs: list[str]) -> int:
        
        # Nesta solução, não é necessário saber em QUAL pasta estamos, ou seja, o caminho
        # Então a melhor solução é apenas com contador, pois a complexidade de espaço torna-se O(1)
        
        # Em uma solução na qual é necessário o caminho final, seria aplicada uma pilha
        
        ans = 0

        for log in logs:

            # Sendo ../, deve retornar 1, mas não pode ser menor que 0
            if log == '../':
                ans = max(0, ans-1)
            # Sendo ./ devemos manter, mas se não for, avança um
            elif log != "./":
                ans += 1

        return ans