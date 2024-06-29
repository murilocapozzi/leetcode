import pytest
from Solution import Solution



def test_example1():
    
    root1 = Solution().arrToTree([3,5,1,6,2,9,8,None,None,7,4])
    root2 = Solution().arrToTree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    
    output = Solution().leafSimilar(root1, root2)
    
    assert output == True
    
def test_example2():
    
    root1 = Solution().arrToTree([1,2,3])
    root2 = Solution().arrToTree([1,3,2])
    
    output = Solution().leafSimilar(root1, root2)
    
    assert output == False