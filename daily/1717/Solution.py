class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeAllSubstrings(s: str, substring: str, gain: int) -> tuple[str, int]:
            # Utiliza uma pilha para verificar sempre se forma a substring
            # ao unir o último elemento da pilha com o novo visto
            # Caso seja verdade, remove da pilha o último, acrescenta os pontos
            # Se não, insere na pilha
            
            score = 0
            stack = []

            for c in s:
                if stack and stack[-1] + c == substring:
                    stack.pop()
                    score += gain
                else:
                    stack.append(c)

            return ''.join(stack), score

        scoreAB = scoreBA = 0
        
        # Começa pela substring que mais ganha pontos, assim os maximiza
        if x > y:
            s, scoreAB = removeAllSubstrings(s, 'ab', x)
            s, scoreBA = removeAllSubstrings(s, 'ba', y)
        else:
            s, scoreBA = removeAllSubstrings(s, 'ba', y)
            s, scoreAB = removeAllSubstrings(s, 'ab', x)

        return scoreAB + scoreBA