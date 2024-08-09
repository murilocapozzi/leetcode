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
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:

        # Casos bases:
        #   se chegou ao fim (None) sem encontrar
        #   se encontrou um dos alvos
        if not root: return None
        if root.val == p or root.val == q: return root.val

        # Desce pelos filhos para tentar achar os alvos
        # O retorno será, temporariamente, o próprio alvo achado 
        isOnLeft = self.lowestCommonAncestor(root.left, p, q)
        isOnRight = self.lowestCommonAncestor(root.right, p, q)

        # Se não está nos dois
        if isOnLeft == None and isOnRight == None:
            return None
        # Se não está na esquerda, está na árvore da direita e vice-versa
        if isOnLeft == None:
            return isOnRight
        if isOnRight == None:
            return isOnLeft
        
        # Quando os dois retornos são diferentes de None, ou seja, os dois foram achados,
        # começa-se a retornar o nó que reuniu os dois, ou seja, o menor parentesco em comum que é a resposta do exercício
        return root.val
        
'''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Solução submetida ao LeetCode
        if not root: return None
        if root == p or root == q: return root

        isOnLeft = self.lowestCommonAncestor(root.left, p, q)
        isOnRight = self.lowestCommonAncestor(root.right, p, q)

        if isOnLeft and isOnRight: return root
        return isOnLeft or isOnRight
'''