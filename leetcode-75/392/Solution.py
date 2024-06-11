class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0
        len_s = len(s)
        len_t = len(t)

        while i < len_t and j < len_s:

            # Itera sobre a string t, incrementando em j se os caracteres de s estão sendo vistos, em ordem
            if j < len_s and s[j] == t[i]:
                j += 1

            i += 1

        # Se j possuir o tamanho da string s, então todos os caracteres foram achados, então é subsequência
        return j == len_s
        