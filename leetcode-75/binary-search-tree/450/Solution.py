# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root: return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # node.val == key
            
            if not root.right: return root.left
            if not root.left: return root.right

            if root.right and root.left:
                p = root.right

                while p.left:
                    p = p.left

                root.val = p.val
                root.right = self.deleteNode(root.right, root.val)

        return root