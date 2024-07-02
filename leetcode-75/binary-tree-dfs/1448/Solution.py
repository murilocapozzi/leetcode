# Definition for a binary tree node.
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
    
    def dfs(self, root, val):
        
        if not root: return 0
        
        # Atualiza qual o maior dos já vistos
        maxVal = max(val, root.val)

        # Percorre a árvore
        left = self.dfs(root.left, maxVal)
        right = self.dfs(root.right, maxVal)

        # Se o valor atual é maior ou igual o maior visto, acrescenta 1
        # Soma-se ao resultado da esquerda e direita
        return 1 + left + right if root.val >= val else left + right

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)