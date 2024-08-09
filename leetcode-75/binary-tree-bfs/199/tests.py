import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([1,2,3,None,5,None,4])
    
    output = Solution().rightSideView(root)
    
    assert output == [1,3,4]
    
def test_example2():
    
    root = Solution().arrToTree([1,None,3])
    
    output = Solution().rightSideView(root)
    
    assert output == [1,3]
    
def test_example3():
    
    root = Solution().arrToTree([])
    
    output = Solution().rightSideView(root)
    
    assert output == []