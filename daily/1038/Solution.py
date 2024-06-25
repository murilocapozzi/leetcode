# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def transform(self, root):
    # TreeNode para Lista
        
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
    
    def __init__(self):
    # Variável da classe que guarda a soma geral de todos os vistos
        self.sum = 0
    
    def transform(self, nums, i=0) -> TreeNode:
    # Lista para TreeNode
        
        left = self.transform(nums, 2*i+1) if 2*i+1 < len(nums) and nums[2*i+1] != None else None
        right = self.transform(nums, 2*i+2) if 2*i+2 < len(nums) and nums[2*i+2] != None else None
        
        return TreeNode(val=nums[i], left=left, right=right)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:

        if root:
            # Desce até a direita
            self.bstToGst(root.right)
            
            # Começa a soma pelo extremo direito
            self.sum += root.val

            # A maior soma vista "até agora" é guardada neste nó
            root.val = self.sum

            # Desce até a esquerda
            self.bstToGst(root.left)

        return root