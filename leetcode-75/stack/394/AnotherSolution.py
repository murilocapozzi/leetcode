class Solution:        
    def decodeString(self, s: str) -> str:
        
        # Pilha que guarda o registro de blocos, pela string obtida antes de ver um número e o número de vezes que irá repetir o próximo bloco
        stack = []
        ans = ""
        n = 0
        
        for c in s:
            
            if c == '[':
            # Se vê um [, é um ínicio novo, empilha o que havia coletado até o momento, sendo o número a cabeça
                stack.append(ans)
                stack.append(n)
                n = 0
                ans = ""
                
            elif c == ']':
            # Se vê um ], é fim de um bloco, desempilha o número e a string que estava antes
                num = stack.pop()
                prevString = stack.pop()
                
                # Multiplica a string atual pelo número desempilhado e concatena com o que estava
                # Não empilha, pois pode continuar a vir caracteres que podem concatenar, ou simplesmente encerrar a string original
                ans = prevString + ans * int(num)
                
            # Ao ver dígitos, transforma-os em inteiro e junta ao montante
            elif c.isdigit(): n = n * 10 + int(c)
            # Ao ver caracteres isolados, concatena-os
            else: ans += c
        
        return ans