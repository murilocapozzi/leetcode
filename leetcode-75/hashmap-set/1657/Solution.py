class Solution(object):    
    def closeStrings(self, word1, word2):
        
        # As letras devem ser as mesmas
        if set(word1) != set(word2):
            return False
        
        occurrencesWord1 = {}
        occurrencesWord2 = {}
        freq1 = []
        freq2 = []
        
        # Pega a quantidade de letras de cada palavra
        for w in word1:
            if w in occurrencesWord1: occurrencesWord1[w] += 1
            else: occurrencesWord1[w] = 1
        for w in word2:
            if w in occurrencesWord2: occurrencesWord2[w] += 1
            else: occurrencesWord2[w] = 1
            
        for occ in occurrencesWord1:
            freq1.append(occurrencesWord1[occ])
            
        for occ in occurrencesWord2:
            freq2.append(occurrencesWord2[occ])
        
        # Ordena a quantidade
        freq1.sort()
        freq2.sort()
        
        # Se a ordenação for igual nas duas palavras, as trocas podem ser feitas então são parecidas
        return freq1 == freq2