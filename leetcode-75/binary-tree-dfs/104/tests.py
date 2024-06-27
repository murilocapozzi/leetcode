import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([3,9,20,None,None,15,7])
    
    output = Solution().maxDepth(root)
    
    assert output == 3
    
def test_example2():
    
    root = Solution().arrToTree([1,None,2])
    
    output = Solution().maxDepth(root)
    
    assert output == 2