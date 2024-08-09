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
    
    def treeToArr(self, root, arr=[]):
        
        if not root: return []
        
        arr.append(root.val)
        self.treeToArr(root.left, arr)
        self.treeToArr(root.right, arr)
        
        return arr
    
    def searchBST(self, root, val):

        if not root: return None
        if root.val == val: return root

        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)

        return left if left != None else right