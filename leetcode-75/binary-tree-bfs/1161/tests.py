import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([1,7,0,7,-8,None,None])
    
    output = Solution().maxLevelSum(root)
    
    assert output == 2
    
def test_example2():
    
    root = Solution().arrToTree([989,None,10250,98693,-89388,None,None,None,-32127])
    
    output = Solution().maxLevelSum(root)
    
    assert output == 2