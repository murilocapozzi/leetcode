# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def arrToTree(self, arr, i=0):
        
        if i >= len(arr) or arr[i] == None: return None
        
        left = self.arrToTree(arr, 2*i+1)
        right = self.arrToTree(arr, 2*i+2)
        
        return TreeNode(val=arr[i], left=left, right=right)
    
    def rightSideView(self, root: TreeNode) -> list[int]:

        # Dicionário que irá armazenar qual o último elemento visto no nível
        # Sendo a key o nível e o value o valor do último visto
        rightMost = {}

        def bfs(node, level):
            if not node: return

            # Atualiza como sendo o último
            rightMost[level] = node.val
            
            # Percorre para esquerda e direita, aumentar em 1 no nível, de forma pré-fixa, ou seja, direita por último
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)

        bfs(root, 0)
        
        # Coleta o value de todos os níveis
        return [values[1] for values in rightMost.items()]