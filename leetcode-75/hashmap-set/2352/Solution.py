from typing import Counter
import numpy as np

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        
        # Transforma a matriz em um dicionário, na qual a chave será uma linha e o valor será a quantidade de vezes que ela se repete na matriz
        
        # Transforma na matriz transporta
        transposeGrid = Counter(zip(*grid))
        
        grid = Counter(map(tuple,grid))
        equals = 0
        
        # Como são dicionários, itera pelas chaves da transposta
        # Se existir o valor na matriz normal, irá multiplicar e descobrir quantas ocorrências iguais
        for row in transposeGrid:
            equals += transposeGrid[row] * grid[row]
        
        return equals