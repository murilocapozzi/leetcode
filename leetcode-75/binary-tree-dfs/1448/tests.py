import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([3,1,4,3,None,1,5])
    
    output = Solution().goodNodes(root)
    
    assert output == 4
    
def test_example2():
    
    root = Solution().arrToTree([3,3,None,4,2])
    
    output = Solution().goodNodes(root)
    
    assert output == 3
    
def test_example3():
    
    root = Solution().arrToTree([1])
    
    output = Solution().goodNodes(root)
    
    assert output == 1