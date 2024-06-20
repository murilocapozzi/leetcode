class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        # Dicionário que irá guardar unicamente quantas vezes cada número repetiu
        occurrences = {}
        # Lista que irá conter a quantidade única. Caso repita, não é único e retorna falso
        quantity = []      
        
        for num in arr:
            if num in occurrences: occurrences[num] += 1
            else: occurrences[num] = 1
        
        for key in occurrences:
            if occurrences[key] in quantity: return False
            quantity.append(occurrences[key])
            
        # Se na lista não entrou nenhuma quantidade repetida, o número de ocorrências é único, retorna verdadeiro
        return True