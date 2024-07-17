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
    
    def treeToArr(self, root, arr, i):
        
        if not root: 
            arr.insert(i, None)
            return
        
        arr.insert(i, root.val)
        if root.left or root.right:
            self.treeToArr(root.left, arr, (2*i) + 1)
            self.treeToArr(root.right, arr, (2*i) + 2)
    
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:

        # Transforma em set para otimizar a busca e para pesquisar na árvore apenas uma vez
        to_delete = set(to_delete)
        ans = []

        def deleteNode(root, is_root):

            if not root: return None

            root_deleted = root.val in to_delete

            # Se o nó atual não está para ser deletado e o anterior foi deletado, insere na resposta
            if is_root and not root_deleted:
                ans.append(root)

            # Continua a busca pelos filhos, com a flag se o nó foi removido ou não
            root.left = deleteNode(root.left, root_deleted)
            root.right = deleteNode(root.right, root_deleted)

            if root_deleted:
                return None
                
            return root

        deleteNode(root, True)
        return ans