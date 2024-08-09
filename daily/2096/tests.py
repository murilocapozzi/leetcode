import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([5,1,2,3,None,6,4])
    startValue = 3
    destValue = 6
    
    output = Solution().getDirections(root, startValue, destValue)
    
    assert output == 'UURL'
    
def test_example2():
    
    root = Solution().arrToTree([2,1])
    startValue = 2
    destValue = 1
    
    output = Solution().getDirections(root, startValue, destValue)
    
    assert output == 'L'