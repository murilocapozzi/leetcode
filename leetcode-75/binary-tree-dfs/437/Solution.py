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
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0

        def calculate(root, val):
        # CALCULATE acumula a soma dos anteriores e incrementa caso seja igual ao targetSum
            if not root: return
            calculate(root.left, root.val + val)
            calculate(root.right, root.val + val)

            if root.val + val == targetSum: self.ans += 1

        def dfs(root):
        # DFS é chamado para iniciar a soma pelo nó dado
        # Isso dá chance para todos os nós serem o início de uma soma
        # Inicia o cálculo com o nó que chegou e chama para os filhos também
            if not root: return

            calculate(root, 0)
            dfs(root.left)
            dfs(root.right)

            
        dfs(root)
        return self.ans