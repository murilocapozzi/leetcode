# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def arrToTree(self, arr, i=0):
        
        if i >= len(arr) or arr[i] == None: return None
        
        left = self.arrToTree(arr, 2*i+1)
        right = self.arrToTree(arr, 2*i+2)
        
        return TreeNode(val=arr[i], left=left, right=right)
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # Função para procurar o valor buscado, já que os valores são únicos.
        # Retorna o caminho da raiz até o nó, encontrado em 'path'
        def dfs(root: Optional[TreeNode], value: int, path: list) -> bool:

            if root.val == value: return True

            if root.left and dfs(root.left, value, path):
                path.append('L')
            elif root.right and dfs(root.right, value, path):
                path.append('R')

            return path

        # Descobre o caminho para o valor de início e o caminho para o valor de destino
        startPath, destPath = [], []
        dfs(root, startValue, startPath)
        dfs(root, destValue, destPath)

        # Neste passo, são removidos os passos em comum do final, ou seja, passos em que
        # já foram os dois encontrados previamente e retornam a raiz juntos
        # No momento em que o último passo dado é diferente, este é o ponto de encontro,
        # o menor caminho possível entre eles
        while startPath and destPath and startPath[-1] == destPath[-1]:
            startPath.pop()
            destPath.pop()

        # Substitui os passos do início por 'U' e inverte o de destino
        # indicando que está indo, e não voltando
        startPath = 'U' * len(startPath)
        destPath = ''.join(destPath[::-1])

        return startPath + destPath