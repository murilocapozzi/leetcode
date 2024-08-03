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
    
    def maxLevelSum(self, root: TreeNode) -> int:
        
        sumLevels = {}

        def bfs(node, level):
            if not node: return

            if level in sumLevels: sumLevels[level] += node.val
            else: sumLevels[level] = node.val

            bfs(node.left, level + 1)
            bfs(node.right, level + 1)

        bfs(root, 1)

        return max(sumLevels, key=sumLevels.get)