class Solution:

    def maxVowels(self, s: str, k: int) -> int:

        if k == 0: return 0
        
        vowels = {"a", "e", "i", "o", "u"}
        actualV = 0

        # Inicializa com os k primeiros
        for i in s[:k]:
            if i in vowels:
                actualV += 1

        maxV = actualV

        for i in range(k, len(s)):

            if maxV == k:
                return k

            # Retira o anterior i - k da janela deslizante
            if s[i-k] in vowels:
                actualV -= 1

            # Adiciona o novo i da janela deslizante
            if s[i] in vowels:
                actualV += 1


            if actualV > maxV:
                maxV = actualV

        return maxV