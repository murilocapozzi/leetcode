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

    def countPairs(self, root: TreeNode, distance: int) -> int:

        self.count = 0
        
        def dfs(root: Optional[TreeNode]) -> list[int]:

            if not root: return []
            # Encontrou uma folha, retorna 1 para inicializar a lista contendo as distâncias
            if not root.left and not root.right: return [1]

            left = dfs(root.left)
            right = dfs(root.right)

            # Analisa elemento a elemento das listas vindas da esquerda e direita
            # Se a soma for menor que o limite, incrementa no contador
            for l in left:
                for r in right:
                    self.count += l + r <= distance

            # Junta as duas listas, incrementando 1 na distância de todas
            join = left + right
            return [i + 1 for i in join]

        dfs(root)
        return self.count
