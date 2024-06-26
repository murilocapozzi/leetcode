# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def transform(self, root):
    # TreeNode para Lista INFIXA
        
        nums = []
        
        if root:
            nums.append(root.val)
        else:
            nums.append(None)
            return nums
            
        nums += self.transform(root.left)
        nums += self.transform(root.right)
        
        return nums

class Solution:
    def treeNodeToList(self, root: TreeNode) -> list[int]:
    # TreeNode para Lista de forma prefixa, ou seja, ordenada de forma decrescente
        nums = []
        
        if root:
            nums += self.treeNodeToList(root.left)
            nums.append(root.val)
            nums += self.treeNodeToList(root.right)
        
        return nums

    def listToTreeNode(self, nums: list[int], start: int, end: int) -> TreeNode:
    # Lista ordenada para TreeNode
        if start > end: return

        mid = (start + end) // 2
        return TreeNode(nums[mid], self.listToTreeNode(nums, start, mid - 1), self.listToTreeNode(nums, mid + 1, end))

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.treeNodeToList(root)
        return self.listToTreeNode(nums, 0, len(nums) - 1)
        