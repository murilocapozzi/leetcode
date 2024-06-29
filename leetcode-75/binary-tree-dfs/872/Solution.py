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
    
    def getLeafs(self, root, leafs):
        
        # Se o nó não possui filhos à esquerda nem à direita, é uma folha
        # Adiciona-o na lista resultante
        if root and not root.left and not root.right:
            leafs.append(root.val)
        elif root:
            
            # Percorre esquerda
            if root.left:
                self.getLeafs(root.left, leafs)
            
            # Percorre direita
            if root.right:
                self.getLeafs(root.right, leafs)
                
        return leafs
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Com a lista resultante dos dois, compara-os e retorna o resultado
        return self.getLeafs(root1, []) == self.getLeafs(root2, [])