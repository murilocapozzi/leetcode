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
    
    def printTree(self, root):
        
        if not root: return
        self.printTree(root.left)
        print(root.val, end=', ')
        self.printTree(root.right)
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        # LEFT: direction == 1
        # RIGHT: direction == 0
        def dfs(root, direction, currZZ, maxZZ) -> int:
            
            if not root :
                # Ao bater em um None, retorna retirando si mesmo da contagem
                print('None', maxZZ, currZZ, max(maxZZ, currZZ) - 1)
                return max(maxZZ, currZZ) - 1
            elif (direction == 0):
                # Veio da direita:
                #   aumenta 1 no currZZ indo para esquerda
                #   reinicia indo para direita
                left = dfs(root.left, 1, currZZ + 1, max(maxZZ, currZZ + 1))
                right = dfs(root.right, 0, 1, max(maxZZ, currZZ + 1))
                print(left, right, max(left, right))
                return max(left, right)
            else:
                # Veio da esquerda
                #   aumenta 1 no currZZ indo para direita
                #   reinicia indo para esquerda
                right = dfs(root.right, 0, currZZ + 1, max(maxZZ, currZZ + 1))
                left =  dfs(root.left, 1, 1, max(maxZZ, currZZ + 1))
                print(left, right, max(left, right))
                return max(left, right)

        # Inicia com 0, então tanto faz o 'left', irá para esquerda e/ou direita com valor 1
        # Retornará o máximo, que sempre é verificado durante as buscas
        return dfs(root, 0, 0, 0)
    
root = Solution().arrToTree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])

Solution().printTree(root)
print()
output = Solution().longestZigZag(root)

print(output)