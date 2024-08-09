import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([10,5,-3,3,2,None,11,3,-2,None,1])
    targetSum = 8
    
    output = Solution().pathSum(root, targetSum)
    
    assert output == 3
    
def test_example2():
    
    root = Solution().arrToTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    targetSum = 22
    
    output = Solution().pathSum(root, targetSum)
    
    assert output == 3