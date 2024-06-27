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
    
    def maxDepth(self, root):
        # Função recursiva, ao chegar em um None, retorna 0
        
        if not root:
            return 0
        
        # Calcula a profundida da esquerda e da direita
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        # Retorna o maior dos filhos + 1, ou seja, mais si próprio
        return max(left, right) + 1
    
        """
        ONE LINE SOLUTION:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
        """